from flask import Flask, render_template, request
import os
import PyPDF2
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load NLP model
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def analyze_resume(resume_text, job_description=""):
    doc = nlp(resume_text)
    skills = list(set(ent.text for ent in doc.ents if ent.label_ == "SKILL"))
    education = list(set(ent.text for ent in doc.ents if "education" in ent.label_.lower()))
    experience = re.findall(r'\d+\+? years?', resume_text.lower())
    
    job_keywords = set(word_tokenize(job_description.lower())) - stop_words
    resume_keywords = set(word_tokenize(resume_text.lower())) - stop_words
    match_score = len(job_keywords & resume_keywords) / len(job_keywords) * 100 if job_keywords else 0
    
    return {
        "skills": skills,
        "education": education,
        "experience": experience,
        "match_score": round(match_score, 2)
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'resume' not in request.files:
            return "No file uploaded", 400
        
        resume = request.files['resume']
        if resume.filename == '':
            return "No file selected", 400
        
        if not resume.filename.lower().endswith('.pdf'):
            return "Only PDF files are allowed", 400
        
        try:
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
            resume.save(resume_path)
            text = extract_text_from_pdf(resume_path)
            os.remove(resume_path)
            
            if not text.strip():
                return "Failed to extract text from PDF", 400
            
            analysis = analyze_resume(text, request.form.get('job_description', ''))
            return render_template('results.html', analysis=analysis)
        except Exception as e:
            return f"Error: {str(e)}", 500
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
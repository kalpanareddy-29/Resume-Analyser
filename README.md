AI-Powered Resume Analyzer
Overview
The AI-Powered Resume Analyzer is a web-based application designed to help HR professionals and students evaluate resumes efficiently. Using Machine Learning (ML) and Natural Language Processing (NLP), the system extracts key skills, experience, and qualifications from resumes, ranks them based on job descriptions, and presents the results in descending order of relevance.

Features
✅ Automated Resume Scoring – Assigns scores to resumes based on job description matching
✅ Keyword Extraction – Identifies key skills, experience, and qualifications
✅ Ranked Output – Displays resumes in descending order of relevance
✅ Web-Based Interface – Built using HTML, CSS, JavaScript, and Flask
✅ Fast Processing – Handles 100+ resumes per batch, ensuring quick analysis

Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

Machine Learning: Scikit-Learn, NLP (spaCy/NLTK), TF-IDF

Data Processing: Pandas, NumPy

Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Application
bash
Copy
Edit
python app.py
Now, open http://127.0.0.1:5000 in your browser.

Usage
Upload a resume PDF and enter the job description.

The system will analyze and score resumes based on relevance.

View the sorted list of resumes from highest to lowest score.

Project Structure
php
Copy
Edit
ai-resume-analyzer/
│── static/             # CSS, JS files  
│── templates/          # HTML templates  
│── uploads/            # Resume uploads  
│── app.py              # Flask Backend  
│── model.py            # ML Model for resume scoring  
│── requirements.txt    # Dependencies  
│── README.md           # Project Documentation  
Contributions
Contributions are welcome! Feel free to fork this repo, submit pull requests, or report issues.

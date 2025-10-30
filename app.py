from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
import os

nltk.download('stopwords')
from nltk.corpus import stopwords

app = Flask(__name__)

# ---------------- Helper Functions ----------------
def extract_text_from_pdf(file):
    text = ""
    pdf = PdfReader(file)
    for page in pdf.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = [word for word in text.split() if word not in stopwords.words('english')]
    return " ".join(words)

def calculate_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

# ---------------- Flask Routes ----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    job_desc = request.form['jobdesc']

    if not resume or not job_desc:
        return "Please upload a resume and enter a job description."

    resume_text = extract_text_from_pdf(resume)
    cleaned_resume = clean_text(resume_text)
    cleaned_job = clean_text(job_desc)

    score = calculate_similarity(cleaned_resume, cleaned_job)

    feedback = ""
    if score > 80:
        feedback = "Excellent match! Your resume fits this role very well."
    elif score > 60:
        feedback = "Good match. You might want to add more relevant keywords."
    else:
        feedback = "Low match. Try tailoring your resume to the job description."

    return render_template('index.html', score=score, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
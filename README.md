AI Resume Analyzer
An AI-powered *Flask web application* that analyzes resumes using *Natural Language Processing (NLP)* to compare them with job descriptions and calculate a *match score*. The tool helps job seekers tailor their resumes for better alignment with specific roles.

Features
- Upload a resume (PDF format)  
- Paste a job description  
- Get an instant match score (0–100%)  
- Receive feedback on how to improve resume relevance  
- Simple and responsive UI built with Bootstrap  

Tech Stack
- Backend: Flask  
- NLP Libraries: NLTK, scikit-learn  
- PDF Parsing: PyPDF2  
- Frontend: HTML, Bootstrap  
- Similarity Measure: TF-IDF + Cosine Similarity  

Installation & Setup

1. Clone the repository
   bash
   git clone https://github.com/<your-username>/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
   

2. Install dependencies
   bash
   pip install -r requirements.txt
   

3. Run the app
   bash
   python app.py
   

4. Open your browser and go to:
   
   http://127.0.0.1:5000
   

How It Works
1. The user uploads a resume and pastes a job description.  
2. The resume text is extracted using *PyPDF2*.  
3. Both texts are cleaned and tokenized using *NLTK*.  
4. Text similarity is computed using *TF-IDF Vectorization* and *Cosine Similarity*.  
5. The match score and tailored feedback are displayed to the user.


Future Enhancements
- Add keyword extraction and recommendations  
- Display detailed skill gaps and strengths  
- Support DOCX resumes  
- Add user authentication for saved reports  

Author
Krutarth Dubey 
📍 Bhopal, India  
📧 [krutarthdubey2001@gmail.com](mailto:krutarthdubey2001@gmail.com)  
🔗 [GitHub](https://github.com/krutarthdubey) | [LinkedIn](https://linkedin.com/in/krutarth-dubey) | [LeetCode](https://leetcode.com/u/cracky123/)

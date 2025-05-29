📄 Resume Scanner & Ranker

A Streamlit web app that helps recruiters (or job seekers) evaluate how well resumes match a job description using NLP and cosine similarity.

Live Demo

👉 [Click here to try the app](https://resume-scanner-mfbbvn3tzcdlraj5mxueiw.streamlit.app/)  

Features

- Upload multiple PDF resumes
- Paste a job description
- Get ranked scores based on content similarity
- Simple, fast UI powered by Streamlit

Tech Stack

- Frontend/UI: Streamlit
- NLP Processing: Scikit-learn, TfidfVectorizer
- PDF Parsing: PyMuPDF (`fitz`)
- Language: Python

📂 Project Structure

- Plaintext
resume-scanner/
├── app.py               Main Streamlit app
├── ranker.py            Contains the resume ranking logic (TF-IDF + cosine similarity)
├── resume_parser.py     Extracts text from PDF resumes using PyMuPDF
├── requirements.txt     Python dependencies
├── .gitignore           Files/folders to ignore in Git
└── README.md            Project documentation

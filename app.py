import streamlit as st
from ranker import rank_resumes
from resume_parser import extract_text_from_pdf

st.title("📄 Resume Scanner & Ranker")

job_desc = st.text_area("Paste Job Description Here")

uploaded_files = st.file_uploader("Upload Resumes (PDF)", accept_multiple_files=True)

if st.button("Rank Resumes") and job_desc and uploaded_files:
    scores = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        score = rank_resumes(job_desc, text)
        scores.append((file.name, round(score, 2)))

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    st.subheader("📊 Ranked Resumes:")
    for name, score in sorted_scores:
        st.write(f"{name}: {score}")
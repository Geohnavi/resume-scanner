from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd, resume_text):
    documents = [jd, resume_text]
    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(documents)
    return cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100
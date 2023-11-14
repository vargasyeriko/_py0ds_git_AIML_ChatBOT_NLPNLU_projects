
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def find_best_match(job_desc, document_titles):
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Combine the job description with the list of document titles
    all_docs = [job_desc] + document_titles
    
    # Generate the TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(all_docs)
    
    # Compute the cosine similarity between the job description and each document title
    cos_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Get the index of the most similar document
    most_similar_idx = np.argmax(cos_similarities)
    
    # Return the title of the most similar document
    return document_titles[most_similar_idx]

# Your list of document titles
document_titles = list_jupy
# Sample job description
str_ref_job_desc = str_ref_job_desc

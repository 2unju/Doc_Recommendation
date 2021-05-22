from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from soylemma import Lemmatizer
from konlpy.tag import Okt

import pandas as pd

def Top10_Docs(docs_df, title):
    okt = Okt()

    tfidif_vectorizer = TfidfVectorizer(
        tokenizer=Okt.nouns,
        ngram_range=(1, 2),
        )
    std_doc = docs_df.iloc[docs_df[title]]
    std_vec = tfidif_vectorizer.fit_transform(std_doc.values.astype('U'))
    doc_vector = tfidif_vectorizer.fit_transform(docs_df['content'].values.astype('U'))
    similarity = []
    for q in doc_vector:
        similarity = cosine_similarity(std_vec, q)

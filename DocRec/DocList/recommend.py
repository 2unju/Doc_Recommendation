from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
# from soylemma import Lemmatizer
from konlpy.tag import Okt

import itertools
import pandas as pd
import os

from .vacabulary import MakeVoca

okt = Okt()


def DocToNouns(docs):
    return [{
        'id': i,
        'nouns': ' '.join(okt.nouns(doc)),
    } for i, doc in enumerate(docs["content"])]


def Top10_Docs(docs_df, id):
    docs_nouns = DocToNouns(docs_df)  # {id: , nouns:}
    # if not os.path.isfile("voca.json"):
    #     MakeVoca(docs_df)
    tfidif_vectorizer = TfidfVectorizer()
    docs_vector = tfidif_vectorizer.fit_transform(doc['nouns'] for doc in docs_nouns)

    std_doc = docs_df.iloc[id - 1, 3]
    std_nouns = okt.nouns(std_doc)
    frequency = {}
    for noun in std_nouns:
        if noun in frequency:
            frequency[noun] += 1
        else:
            frequency[noun] = 1
    frequency = sorted(frequency.items(), key=(lambda x: x[1]), reverse=True)

    std_vec = docs_vector[id - 1]
    similarity = cosine_similarity(std_vec, docs_vector)
    similarity = list(itertools.chain.from_iterable(similarity))

    similarity_rank = [[i, doc] for i, doc in enumerate(similarity)]
    similarity_rank.sort(key=lambda x: x[1], reverse=True)

    Top10 = []
    titles = docs_df['title']
    print(titles)
    for idx in similarity_rank:
        if len(Top10) == 10:
            break
        # print (docs_df.iloc[idx[0]])
        doc = titles[idx]
        if doc in Top10:
            continue
        # doc['id'] = idx[0]
        Top10 +=doc

    return Top10, frequency


def SearchDoc(docs_df, word):
    ranking = {}
    idx = 0
    for doc in docs_df['content']:
        doc_nouns = okt.nouns(doc)
        ranking[idx] = 0
        for noun in doc_nouns:
            if word == noun:
                ranking[idx] += 1
        idx += 1
    ranking = sorted(ranking.items(), key=(lambda x: x[1]), reverse=True)
    doc_list = []
    idx = 0
    for rank in ranking[:20]:
        doc = docs_df.iloc[rank[0]]
        doc_list.append([idx, doc['title'], doc['url'], doc['content']])
        idx += 1
    return doc_list
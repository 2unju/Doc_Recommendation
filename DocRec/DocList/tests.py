from django.test import TestCase

# Create your tests here.
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt

from .vacabulary import MakeVoca
from .database import GetDF

okt = Okt()
def DocToNouns(docs):
    return [{
        'id': i,
        'nouns': ' '.join(okt.nouns(doc)),
    } for i, doc in enumerate(docs["content"])]

docs_vector = []
if not docs_vector:
    docs_df = GetDF()
    docs_nouns = DocToNouns(docs_df) #{id: , nouns:}
    tfidif_vectorizer = TfidfVectorizer()
    docs_vector = tfidif_vectorizer.fit_transform(doc['nouns'] for doc in docs_nouns)

    # if not os.path.isfile("voca.json"):
    #    MakeVoca(docs_df)


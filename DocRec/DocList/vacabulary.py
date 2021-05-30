import os
import json

from konlpy.tag import Okt

def MakeVoca(nouns_df):
    print("Make Vocabulary")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    okt = Okt()
    id = 1
    nouns_dict = {}
    for doc in nouns_df["content"]:
        nouns_dict[id] = okt.nouns(doc)
        id += 1
    voca = {}
    id = 1
    for nouns in nouns_dict.values():
        for noun in nouns:
           if noun not in voca.values():
                voca[id] = noun
                id += 1
    with open(os.path.join(BASE_DIR + '/', 'voca.json'), 'w+',
              encoding='UTF-8-sig') as json_file:
        json.dump(voca, json_file, ensure_ascii=False)
import argparse

from sklearn.feature_extraction.text import TfidfVectorizer

#import database
from . import database

def main():
    parser = argparse.ArgumentParser(description='Documents Recommendation')
    parser.add_argument(
        '--site',
        default='daum',
        choices=[
            'naver',
            'daum',
            'google',
            'all'
        ],
        type=str,
        help='name of site for getting docs'
    )
    parser.add_argument(
        '--field',
        default='ranking',
        choices=[
            'ranking',
            'politics',
            'society',
            'economic',
            'foreign',
            'culture',
            'it',
        ],
        type=str,
        help='field to read'
    )
    parser.add_argument(
        '--n',
        default=1000,
        type=int,
        help='num of docs'
    )
    parser.add_argument(
        '--tokenizer',
        default='nouns',
        choices=[
            'nouns',
            'pos',
            'morphs',
        ],
        type=str,
        help='konlp tokenizer'
    )
    args=parser.parse_args()

    docs, num = database.GetData(args)
    database.SaveData(docs, num)
    # print(docs_df)
    #select_doc = docs_df.iloc[10]['title']
    # related = Top10_Docs(docs_df, 5)
    # print("title: ", docs_df.loc[5][1])
    # print("related docs: ", related)

if __name__ == '__main__':
    main()
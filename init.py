import os
import argparse
from datetime import datetime, timedelta

from . import DocList


def GetData(args):
    num = 0
    if args.site == 'daum' and args.field == 'rank':
        url = 'https://news.daum.net/ranking/popular?regDate='
        selector = '#mArticle > div.rank_news > ul.list_news2 > li > a'
        _selector = '#harmonyContainer > section > p'
        while num < args.n:
            time = datetime.today()-timedelta(num)
            DocList.GetDocs(url+(time.strftime("%Y%m%d")),
                            selector, _selector)

def main():
    parser = argparse.ArgumentParser(description='Documents Recommendation')
    parser.add_argument(
        '--site',
        default='all',
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
    args=parser.parse_args()

    GetData(args)

if __name__ == '__init__':
    main()
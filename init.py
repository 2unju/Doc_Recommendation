import os
import argparse

from database import GetData

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
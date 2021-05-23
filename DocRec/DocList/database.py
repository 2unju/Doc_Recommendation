import pandas as pd
import psycopg2
#import gensim

from datetime import datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup

def GetData(args):
    docs_df = pd.DataFrame(columns=['idx', 'title', 'url', 'content'])
    print("GetTitle")
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome('chromedriver.exe', options=options)

    num = 0

    if args.site == 'daum' and args.field == 'ranking':
        url = 'https://news.daum.net/ranking/popular?regDate='
        selector = '#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a'
        _selector = '#harmonyContainer > section > p'
        while num < args.n:
            print("num: ", num)
            time = datetime.today()-timedelta(num // 50)
            _url = url + time.strftime("%Y%m%d")

            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            Docs = soup.select(selector)

            for title in Docs:
                if 'NaN' in title:
                    continue
                curl = title.get('href')
                driver.get(curl)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                #content = soup.select(_selector)
                all_content_tags = soup.find_all('p', attrs={'dmcf-ptype': 'general'})
                content = [c.text for c in all_content_tags]
                content = "".join(content)
                docs_df = docs_df.append(pd.DataFrame([[num, title.text, curl, content]],
                                                      columns=['idx', 'title', 'url', 'content']),
                                         ignore_index=True)
                num=num+1

        return docs_df


def SaveData(docs_df):
    sign_info = "host='localhost' dbname ='docdb' user='postgres' password='********'"
    sign = psycopg2.connect(sign_info)
    cursor = sign.cursor()

    cursor.execute("DROP TABLE IF EXISTS doclist")
    cursor.execute("CREATE TABLE doclist (id SERIAL PRIMARY KEY, title TEXT, url TEXT, content TEXT);")
    sign.commit()

    for idx in range(100):
        command = "INSERT INTO doclist (title, url, content)" \
                  "VALUES (%s, %s, %s)"
        cursor.execute(command, (str(docs_df.iloc[idx]['title']),
                                 str(docs_df.iloc[idx]['url']),
                                 str(docs_df.iloc[idx]['content'])))
        sign.commit()

    cursor.close()
    sign.close()


def GetDF():
    sign_info = "host='localhost' dbname ='docdb' user='postgres' password='********'"
    sign = psycopg2.connect(sign_info, cursor_factory=psycopg2.extras.DictCursor)
    cursor = sign.cursor()

    sql = "SELECT * FROM doclist"
    cursor.execute(sql)
    docs = cursor.fetchall()
    cursor.close()
    sign.close()

    docs_df = pd.DataFrame(columns=['idx', 'title', 'url', 'content'])

    for doc in docs:
        docs_df = docs_df.append(pd.DataFrame([[doc[0], doc[1], doc[2], doc[3]]],
                                              columns=['idx', 'title', 'url', 'content']),
                                             ignore_index=True)

    return docs_df
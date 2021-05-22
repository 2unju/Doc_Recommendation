import pandas as pd
import psycopg2
import gensim

from datetime import datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup

def GetData(args):
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome('C:/Users/E_N__/Desktop/chromedriver.exe', options=options)

    num = 0
    docs_df = pd.DataFrame(index=range(0, 3), columns=['title', 'url', 'content'])

    if args.site == 'daum' and args.field == 'ranking':
        url = 'https://news.daum.net/ranking/popular?regDate='
        selector = '#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a'
        _selector = '#harmonyContainer > section > p'
        while num < args.n:
            time = datetime.today()-timedelta(num % 20)
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
                docs_df = docs_df.append(pd.DataFrame([[title.text, curl, content]],
                                                      columns=['title', 'url', 'content']),
                                                      ignore_index=True)
            num = num + 20


def SaveData(docs_df):
    sign_info = "host='localhost' dbname ='docdb' user='root' password='2019102177'"
    sign = psycopg2.connect(sign_info)
    cursor = sign.cursor()

    cursor.execute("DROP TABLE IF EXISTS doclist")
    cursor.execute("CREATE TABLE doclist (id SERIAL PRIMARY KEY, title TEXT, url TEXT, content TEXT);")
    sign.commit()

    for title in titles:
        command = "INSERT INTO doclist (title, url, content)" \
               "VALUES (%s, %s, %s)"
        cursor.execute(command, (title, titles[title], contents[title]))
        sign.commit()

    cursor.close()
    sign.close()
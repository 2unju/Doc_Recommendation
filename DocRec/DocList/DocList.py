from selenium import webdriver
from bs4 import BeautifulSoup

from Doc_Recommendation.DocRec.DocList import content


def GetDocs(url, selector, _selector):
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #naverNews:'#_newsList > ul > li > div > a'
    Docs = soup.select(selector)

    Doclist = {}
    contents = {}
    for title in Docs:
        _url = title.get('href')
        Doclist[title.text] = title.get(_url)
        contents[title.text] = content.GetContent(_url, _selector)

    return Doclist, contents
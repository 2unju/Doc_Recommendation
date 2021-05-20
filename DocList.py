from selenium import webdriver
from bs4 import BeautifulSoup

def GetDocs(url):
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #naverNews
    Docs = soup.select('#_newsList > ul > li > div > a')

    Doclist = {}
    for title in Docs:
       Doclist[title.text] = title.get('href')

    return Doclist
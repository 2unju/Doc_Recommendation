from selenium import webdriver
from bs4 import BeautifulSoup

def GetContent(url):
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #naverNews
    content = soup.select_one('#newsEndContents')
    res = ""
    for para in content.contents:
        stripped = str(para).strip()
        if stripped == "":
            continue
        if stripped[0] not in ["<", "/"]:
            res += str(para).strip()
    res.replace("&apos;", "")

    return res
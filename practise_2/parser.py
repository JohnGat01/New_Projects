import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.ua/nedvizhimost/kvartiry-komnaty/kiev/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           }

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def parce():
    html = get_html(URL)
    print(html)


parce()


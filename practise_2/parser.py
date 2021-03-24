import requests
from bs4 import BeautifulSoup
from requests.models import Response

URL = "https://www.olx.ua/nedvizhimost/kvartiry-komnaty/kiev/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           }
HOST = 'https://www.olx.ua'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='wrap')
    olx = []
    for item in items:
        olx.append({
            'title': item.find('div', class_='space rel').get_text(strip=True),
            'link': item.find('a', class_='marginright5').get('href'),
            'Price': item.find('p', class_='price').get_text(strip=True),
            'City and time': item.find('td', class_='bottom-cell').get_text(strip=True),
        })
    return olx


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        olx = get_content(html.text)
    else:
        print('Error')


parse()

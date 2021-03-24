import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.olx.ua/transport/legkovye-avtomobili/acura/kiev/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           }
FILE = 'olx_parse.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    # function is scrolling pages
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='item fleft')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='wrap')
    olx = []
    for item in items:
        olx.append({
            'title': item.find('div', class_='space rel').get_text(strip=True),
            'link': item.find('a', class_='marginright5').get('href'),
            'price': item.find('p', class_='price').get_text(strip=True),
            'city and time': item.find('td', class_='bottom-cell').get_text(strip=True),
        })
    return olx


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'link', 'price', 'city and time'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['city and time']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        olx = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count+1):
            print(f'Parcing...Page {page} out of {pages_count}')
            html = get_html(URL, params={'page': page})
            olx.extend(get_content(html.text))
        save_file(olx, FILE)
        print(f'Got {len(olx)} matches')
    else:
        print('Error')


parse()

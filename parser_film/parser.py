#скачать bs4 скачать request
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

URL = "http://www.manascinema.com"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='short_movie_info')
    manas = []

    for i in items:
        manas.append({
            "title":i.find('div', class_='m_title').get_text(),
            'image':URL + i.find('div', class_='m_thumb').find('img').get('src')
        })

    return manas

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code==200:
        manas2 = []
        for i in range(0,1):
            html = get_html(f'http://www.manascinema.com/movies', params=i)
            manas2.extend(get_data(html.text))
            print(manas2)

parser()
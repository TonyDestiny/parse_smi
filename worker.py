from urllib.parse import urljoin
import traceback

from bs4 import BeautifulSoup
import requests
from dateparser import parse

from app.write_in_database import write_exception, write_news

part_url = 'https://mosmetro.ru/'
url = 'https://mosmetro.ru/press/news/'


if __name__ == '__main__':
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find_all('a', class_='newslist__link')
    found_link = len(list(html))
    data = []
    exception = []

    for i in list(html):
        news_url = urljoin(part_url, i['href'])
        news_page = requests.get(news_url)

        try:
            soup = BeautifulSoup(news_page.content, 'html.parser')
            title = soup.find('h1', 'pagetitle__content-title')
            date = soup.find_all('div', {'class': 'pagetitle__content-date'})
            text = '\n'.join([e.text.replace('\n', '') for e in soup.find_all('div', {'class': 'usercontent'}) if
                              e.text is not None])

            data.append({
                'date_publication': parse(date[0].get_text()).strftime('%Y-%m-%d'),
                'title': title.get_text(),
                'text': text,
                'url': news_url
            })
        except Exception:
            exception.append({
                'traceback': traceback.format_exc(),
                'url': news_url,
            })

    write_news(data)
    write_exception(exception)

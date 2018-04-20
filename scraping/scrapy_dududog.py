import time
import csv
import requests
from bs4 import BeautifulSoup


def get_list(page_num, file):
    print('现在位置：第', page_num, '页。')
    url = 'http://dududog.com/find/all?page=' + str(page_num)

    # if requests.get(url).status_code != 200:
    #     raise AttributeError('网站又挂了，我去！')

    html_data = requests.get(url)

    soup = BeautifulSoup(html_data.content, 'lxml')
    div_item = soup.find('div', {'id': 'books'})
    item_lists = div_item.find_all('div', {'class': 'thumbnail'})

    for item in item_lists:
        book_name = item.find('div', {'class': 'topic'}).text
        book_author = item.select('div > p')[0].text
        book_url = item.find('a').get('href')

        file.writerow([book_name.strip('\r\n'),
                       book_author.replace('\t', '').strip('\r\n'),
                       book_url.replace('..', 'http://dududog.com').strip('\r\n')])
    time.sleep(5)


if __name__ == '__main__':
    writer = csv.writer(open('mobibook2.csv', 'w', encoding='utf-8', newline=''))
    for page in range(0,263):
        get_list(page + 1, writer)

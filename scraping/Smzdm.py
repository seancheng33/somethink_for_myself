'''
获取什么值得买网站上的信息，并将其保存
详情页的获取，有待分析，但是索引页的内容已经可以正常获取
'''

import requests
from bs4 import BeautifulSoup



def main():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    data = requests.get('https://faxian.smzdm.com/9kuai9/', headers=headers)
    soup = BeautifulSoup(data.content, 'lxml')

    data_div = soup.find_all('div', {'class': 'feed-block-ver '})

    for item in data_div:
        title = item.find('h5', {'class': 'feed-ver-title'})
        url = title.find('a').get('href')
        source_site = item.find('a', {'class': 'tag-bottom-right'}).text
        date = item.find('div', {'class': 'feed-ver-date'}).text
        descripe = get_descripe(url)
        print(title.text, url, source_site, date, descripe.replace(' ','').replace('\n',''))

def get_descripe(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.content, 'lxml')
    block = soup.find_all('div',{'class':'item-box'})
    for i in block:
        print(i.text)

    return block[0].text

if __name__ == '__main__':
    main()
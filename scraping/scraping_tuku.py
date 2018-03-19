from time import sleep

import requests
from bs4 import BeautifulSoup

def get_chapterlist(url):
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text,'lxml')
    chapterlist_data = soup.find('div',{'id':'chapterlistload'})
    chapterlist = chapterlist_data.find_all('a',{'class':'ib'})
    for chapter in chapterlist:
        chapter_name = chapter.text
        chapter_url = chapter.get('href')
        print(chapter_name,chapter_url)

    return chapterlist

def get_chapterdetail(url):
    #还是要用phantomjs来获取，直接requests，还没有分析出来
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, 'lxml')
    img_url = soup.find('img',{'id':'cp_image'}).get('src')
    base_url = img_url.replace(img_url.split('/')[-1],'')
    num = img_url.split('/')[-1].split('.')[0]
    img_name = img_url.split('.')[-1]

    # print(base_url+str(num)+'.'+img_name)
    while True:
        try:
            pic_url = base_url+str(num).zfill(3)+'.'+img_name #zfill()方法用于给数字前面补了，这里的数字是3位数的，需要补零
            if requests.get(pic_url).status_code ==200:
                with open(str(num).zfill(3)+'.'+img_name,'wb') as imgf:
                    imgf.write(requests.get(pic_url).content)
                num = int(num)+1
                sleep(5)#需要休眠时间，不然会被反爬虫禁止访问一段时间
            else:
                print('没有了，退出')
                break
        except requests.HTTPError as httpError:
            print(str(httpError))
            break




    # print(img_url.get('src'))

if __name__ == '__main__':
    # url = 'http://www.tuku.cc/comic/28/'
    # get_chapterlist(url)

    url = 'http://www.tuku.cc/comic/28/20'
    get_chapterdetail(url)
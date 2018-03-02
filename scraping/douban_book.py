'''
获取豆瓣读书TOP250的内容的爬虫
使用了 requests 和 BeautifulSoup
只是简单的做了把内容读取出来后打印出来而已。
可以继续深化下去，将数据保存到文件或者数据库中。
'''
import requests
from bs4 import BeautifulSoup

def get_book(page):
    url = 'https://book.douban.com/top250?start='+str(page*25) #每页25条数据，所以这里的网址是页码乘以25
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text,'lxml')

    items = soup.find_all("tr",{"class":"item"})

    for item in items:
        title = item.div.a.text.replace('\n','').replace(' ', '') # 书名，页面上的内容存在很多不合理的换行和空格，需要做处理
        ratingNum = item.find("span",{"class":"rating_nums"}) # 评分
        inq = item.find("span", {"class": "inq"}) #短评
        pl = item.find("span", {"class": "pl"})  # 评论人数，内容存在很多不合理的换行和空格，需要做处理
        print('书名：',title)
        print("出版信息：",item.p.text)
        print('评分：',ratingNum.text)
        print('评论人数：', pl.text.replace('\n','').replace(' ', ''))
        if inq == None:
            #存在没有短评的现象，所以这里需要做判断，没有短评会返回一个None
            print('短评：',None)
        else:
            print('短评：', inq.text)
        print('---------------------------')

if __name__ == '__main__':
    for i in range(10):
        # 一页25条数据，所以是循环10次就可以把全部250条数据都拿下来。
        get_book(i)
'''
测试下载图片的功能，就采取中国气象网的图片频道的内容来做下载
'''
import requests,os,time
from bs4 import BeautifulSoup
from selenium import webdriver


def img_index_list(url):
    #获取索引预览页面上的所有图片信息
    html_data = requests.get(url)

    soup = BeautifulSoup(html_data.text,'lxml')

    items = soup.find_all('div',{'class':'oi'})
    img_list = []

    for item in items:
        img_tmp = {}
        img_url = item.find('a').get('href')# 图片的网站
        img_num = item.find('span').text#  图片张数
        img_title = item.find('a').get('title')# 图片的网站标题

        img_tmp['img_url'] = img_url
        img_tmp['img_num'] = img_num
        img_tmp['img_title'] = img_title.replace(' ','')
        img_list.append(img_tmp)

    return img_list

def download_picture(url,title):
    #暂时未知，没有关闭浏览器，迭代，为何会只是获取同一个图片，但是关闭了就是正常
    #此功能有待优化和改善
    cap = webdriver.DesiredCapabilities.PHANTOMJS
    # cap["phantomjs.page.settings.resourceTimeout"] = 100
    # cap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
    cap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    driver = webdriver.PhantomJS(executable_path=os.path.abspath('../phantomjs.exe'), desired_capabilities=cap)
    driver.get(url)

    img_url = driver.find_element_by_xpath('//*[@id="picFullScreen"]').get_attribute('data-src')
    print('下载地址',img_url,'的图片')
    filename =img_url.split('/')[-1] #获取图片名
    #下载并本地保存图片
    if not os.path.exists(title):
        os.mkdir(title+'\\')

    with open(os.path.join(title,filename),'wb') as img_file:
        img_file.write(requests.get(img_url).content)

    driver.quit()

def get_total_pages(url):
    #获取页面下面的页码，去重后返回
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, 'lxml')
    total_num =soup.find('div',{'class','manu mt10'})
    num_url = total_num.find_all('a')
    url_list = []
    for item in num_url:
        url_list.append(item.get('href'))

    return list(set(url_list))

if __name__ == '__main__':
    url_list = get_total_pages('http://p.weather.com.cn/zrds/index.shtml')

    list = []
    for url in url_list:
        list= list+(img_index_list(url))

    # print(list)

    for item in list:
        print('开始下载',item['img_title'],'的图片')
        for i in range(1,int(item['img_num'][:-1])+1):
            url = item['img_url']+'#p='+str(i)
            title = item['img_title']
            download_picture(url,title)

'''
抓取什么值得买网址的9块9的信息
使用phantomjs插件，然后将抓取的内容保存到一个csv文件中，这个只是一个雏形，未完善内容。
后续有一个不用插件，直接用requests模块的版本。
'''
from selenium import webdriver
import csv,time,sys,os

#定义文件存放的路径
filedir = './data/'+time.strftime('%Y%m%d', time.localtime(time.time()))
#如果路径不存在，先创建对应的路径
if not os.path.exists(filedir):
    os.makedirs(filedir)

filename = filedir + '/' + time.strftime('%H%M', time.localtime(time.time())) + '.csv'

csvfile =open(os.path.abspath(filename),'w',encoding='utf-8')
writer = csv.writer(csvfile)

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 100
# cap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
cap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.PhantomJS(executable_path=os.path.abspath('./phantomjs'),desired_capabilities=cap)

def getdata(driver,url):

    #driver.set_page_load_timeout(10)
    driver.get(url)
    datas = driver.find_elements_by_xpath('//*[@id="feed-main-list"]/li/div')
    #整个区域的取下来，防止数据重组的时候对应不正确的问题
    #print(datas)
    for data in datas:
        title = data.find_element_by_class_name('feed-ver-title')
        price = data.find_element_by_class_name('z-ellipsis')
        descripe = data.find_element_by_class_name('feed-ver-descripe')
        link = title.find_element_by_tag_name('a').get_attribute('href')
        shop = data.find_element_by_class_name('tag-bottom-right')
        writer.writerow([title.text, price.text,shop.text, descripe.text,link])

# print('==================faxian======================')
getdata(driver,"https://faxian.smzdm.com/")
# print('==================9kuai9======================')
getdata("https://faxian.smzdm.com/9kuai9/")

csvfile.close()
driver.quit()
sys.exit(0)

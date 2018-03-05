'''
获取汕头气象（http://www.st12121.net）的实时天气信息
通过phantomjs获取，然后保存到一个sqlite文件中。
'''
import csv, os, sys ,time
import sqlite3

from bs4 import BeautifulSoup
from selenium import webdriver

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 100
# cap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
cap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.PhantomJS(executable_path=os.path.abspath('phantomjs.exe'),desired_capabilities=cap)

driver.get('http://www.st12121.net/')

content = driver.find_element_by_xpath('//*[@id="tem_wind"]')

data = BeautifulSoup(content.get_attribute('innerHTML'),'lxml')

temp = data.find_all('div')[3]['title']# 温度
winddata = data.find_all('li')#
wind = ' '.join((winddata[0].text,winddata[1].text,winddata[2].text))#风力
table = data.find_all('div')[-1]#
pressure=table.find_all('tr')[0].text.replace('\n','')#气压
visibility =table.find_all('tr')[1].text.replace('\n','')#能见度
prcp =table.find_all('tr')[2].text.replace('\n','')#时雨量
relative_humidity = table.find_all('tr')[3].text.replace('\n','')#相对湿度

nowtime = time.strftime('%Y%m%d-%H%M',time.localtime(time.time()))

# with open('data/weather.csv','a',encoding='utf-8',newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow([nowtime,temp,wind,pressure,visibility,prcp,relative_humidity])

with sqlite3.connect('data/stweather.db')as conn:
    try:
     c = conn.cursor()
     c.execute("INSERT INTO shantou (time, temp, wind, pressure, visibility, prcp, relative_humidity) VALUES (?,?,?,?,?,?,?)",
               (nowtime, temp[3:], wind, pressure[4:], visibility[5:], prcp[5:], relative_humidity[4:]))
    except sqlite3.OperationalError:
        c.execute(
            "CREATE TABLE shantou (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,time  TEXT,temp  TEXT,wind  TEXT,pressure  TEXT,visibility  TEXT,prcp  TEXT,relative_humidity  TEXT);")
        c.execute(
            "INSERT INTO shantou (time, temp, wind, pressure, visibility, prcp, relative_humidity) VALUES (?,?,?,?,?,?,?)",
            (nowtime, temp[3:], wind, pressure[4:], visibility[5:], prcp[5:], relative_humidity[4:]))
driver.quit()

sys.exit(0)

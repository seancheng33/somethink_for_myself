"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/12/29
@Program      : 获取指定网页中国省市县地区代码，并且将其按照指定的格式保存。
"""
import requests
from bs4 import BeautifulSoup

htmldate = requests.get('http://www.ip33.com/area_code.html')
htmldate.encoding = 'utf-8'
soup = BeautifulSoup(htmldate.text, 'lxml')

citys = soup.find_all("div", {"class": "ip"})

for city in citys:
    filename = city.find("h4").text.split(" ")[0]
    with open(filename + ".txt", 'w', encoding='utf-8') as f:
        f.write(city.find("h4").text + '\n')
        locations = city.find("ul")

        for location in locations:
            t1 = location.find("h5")
            t2 = location.find("ul")
            if t1 == -1 or t2 == -1:
                continue
            else:
                f.write('\n')
                f.write(t1.text + '\n')
                t3 = t2.find_all("li")
                if len(t3) == 0:
                    continue
                else:
                    for t4 in t3:
                        f.write(t4.text + '\n')

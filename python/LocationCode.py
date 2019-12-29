"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/12/29
@Program      : 获取指定网页中国省市县地区代码，并且将其按照指定的格式保存。到以省份命名的txt文件中。
"""
import requests
from bs4 import BeautifulSoup

# 获取地区代码的网址
htmldate = requests.get('http://www.ip33.com/area_code.html')
htmldate.encoding = 'utf-8'     # 该网站需要指定编码，否则乱码
soup = BeautifulSoup(htmldate.text, 'lxml')

# 该网页的内容是在一个class为ip的div层，直接查找出这些div层的内容出来
citys = soup.find_all("div", {"class": "ip"})

# 遍历出各省下面的各市的内容，并将它们打印出来。
for city in citys:
    filename = city.find("h4").text.split(" ")[0]
    # 获取省份名，将其作为要保存的文件名。
    with open(filename + ".txt", 'w', encoding='utf-8') as f:
        f.write(city.find("h4").text + '\n')
        locations = city.find("ul")
        # 遍历出市下面的区、县的内容
        for location in locations:
            t1 = location.find("h5")
            t2 = location.find("ul")
            # 存在一些标签里面是没有内容的，需要跳出这些内容的循环，否则下面的执行会报错。
            if t1 == -1 or t2 == -1:
                continue
            else:
                f.write('\n')
                f.write(t1.text + '\n')
                t3 = t2.find_all("li")
                # 和上面同理，需要跳出没有内容的标签的循环。否则报错。
                if len(t3) == 0:
                    continue
                else:
                    for t4 in t3:
                        f.write(t4.text + '\n')
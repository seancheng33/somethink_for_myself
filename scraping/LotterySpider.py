import sqlite3

import requests, json, time
from bs4 import BeautifulSoup

'''获取中彩网的双色球的开奖信息'''
url = 'http://kj.zhcw.com/kjData/2012/zhcw_ssq_index_last30.js'  # 中彩网的这个文件保存了最近30期的双色球开奖数据
web_data = requests.get(url).content
soup = BeautifulSoup(web_data, 'lxml')

datatmp = str(soup.select('p')).split('var')[1]  # 第二段内容为无序的近30期的开奖记录数据
datatmp2 = datatmp[24:-11]  # 去掉一些没用的信息
issuetmp = str(soup.select('p')).split('var')[3]  # 第三段内容为期号的信息

jsondata = json.loads(datatmp2)

issue = issuetmp[15:22]  # 截取排在第一个的期号，因为期号是按顺序排序的，取得第一个就是最新一期

kjdate = jsondata[issue]['kjDate']  # kjDate的字段为开奖时间
gamename = jsondata[issue]['czName']  # czName为游戏名称的字段

# kjZNum为红球的字段，字段是按照摇出来的顺序排序的,用split()将字符串去掉空格变成list，再用sorted()排序
redball = sorted(jsondata[issue]['kjZNum'].split())
blueball = jsondata[issue]['kjTNum']  # kjTNum为蓝球的字段

# 和我自己的号码做对比，求红球的交集
myredball = ['02', '04', '13', '20', '25', '32']
myblueball = '6'

red = list(set(redball).intersection(set(myredball)))  # 校对两个list中的合集
# print(len(red))
# print(blueball == myredball)

# # 将获取到的所需字段自己组合成比较明晰清楚的信息出来，redball是一个list，要变成字符串才能一起组合
# message = "彩票名称：" + gamename + "，期号：" + issue + "，开奖时间：" + kjdate + "，\n红球号码： " + str(
#     redball) + "，蓝球号码： " + blueball + "\n"
# message2 = "红球中 " + str(len(red)) + " 个号码，蓝球中奖？" + str(blueball == myblueball)
#
# currentdate = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 获取当前日期，在后面可用于保存数据用来做文件名
#
# # print(message)
# # print("当前时间： " + currentdate)
#
# # 将以上数据组合后保存在“当前日期.txt”的文件中
# f = open(currentdate + ".txt", 'w')
# f.write(message)
# f.write(message2)
# f.close()

with sqlite3.connect('data/lotterydb.db') as conn:
    c = conn.cursor()
    try:
        c.execute("INSERT INTO unionlotto (issue,kjdate,redball,blueball) VALUES (?,?,?,?)",
                  (issue, kjdate, ' '.join(redball), blueball))
    except sqlite3.OperationalError:
        c.execute(
            "CREATE TABLE 'unionlotto' (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,issue  TEXT,kjdate  TEXT,redball  TEXT,blueball  TEXT);")
        c.execute("INSERT INTO unionlotto (issue,kjdate,redball,blueball) VALUES (?,?,?,?)",
                  (issue, kjdate, ' '.join(redball), blueball))
'''
双色球中奖规则，准备再做一个校验，直接告诉我，中了多少钱
一等奖：中6+1。当期高奖级奖金的75%（当奖池资金低于1亿元时，一等奖单注封顶500万元；当奖池资金高于1亿元（含）时，一等奖单注封顶1000万元
二等奖：中6+0。当期高奖级奖金的25%
三等奖：中5+1。单注奖金3000
四等奖：中5+0或中4+1。单注奖金200
五等奖：中4+0或中3+1。单注奖金10
六等奖：中2+1或中1+1或中0+1。单注奖金5
'''

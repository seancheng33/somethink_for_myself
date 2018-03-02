'''
输入京东的产品编码，获取该产品的评论信息，保存为一个comment.txt的文件。
简单用sleep停止随机的数秒，算是简易的干扰反爬虫策略。
'''
import random,requests, time

pagenum = 0
url = 'https://sclub.jd.com/comment/productPageComments.action'
content_list = []
while pagenum < 100:
    #只取10页，也就是100条的评论，没有人会有耐心看几万条评论，100条应该足够分析出一些问题，如果不够，改大该数值就可以了
    data = {
        # 'callback': 'fetchJSON_comment98vv29625',
        'productId': 2857483, # 产品编码，很容易可以在正常的浏览的url地址获得
        'score': 0,
        'sortType': 5, # 排序类型
        'page': pagenum,# 页码
        'pageSize': 10, # 每页显示的评论条数，貌似修改无效，都是每行十条
        # 'isShadowSku': 0,
        # 'fold': 1
    }
    r = requests.get(url, params=data)
    s = r.json()
    comments_list = s['comments']

    if len(comments_list) ==0:
        #返回的数据条数为0，就是表示已经没有数据了，可以跳出这个循环，完成爬取
        break

    for comment in comments_list:
        content_list.append(comment['content'].replace('\n',''))
        # print(comment['content'],comment['creationTime'],comment['referenceName'],
        #       comment['referenceTime'],comment['nickname'],comment['userLevelName'],comment['score'],)

    sec = random.randint(5, 10) #停5~10秒，使整个过程看起来更像人工的浏览，简易的干扰反爬虫机制手段。
    time.sleep(sec)
    pagenum += 1

with open('comment.txt','w',encoding='utf-8') as f:
    for item in content_list:
        f.write(item+'\n')

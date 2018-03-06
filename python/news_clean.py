'''
这个脚本是将一个news.json的文件的几万条数据给分别读取出来，然后分类放置在不同的文件夹中。
仅十几行内容而已。
为一个练习中文分类的机器学习做数据整理的准备工作的脚本
'''
import json,os

with open('News.json', encoding='utf-8') as jsonfile:
    jsondata = json.load(jsonfile)
    # 导出的文件，都是在一个RECORDS的项里面
    for item in jsondata['RECORDS']:
        # 遍历每一条数据
        filename = item['ArticleId']  # 将ArticleId作为文件名
        content = str(item['ArticleTitle']) +'\r\n'+ str(item['ArticleText'])  # 标题和正文是写到文件中的正文内容
        lable = item['Categorization'].strip()  # 按照这个分类来建立分类的文件夹
        #先判断文件夹是否存在，如果不存在就建立一个文件夹
        if not os.path.exists(lable):
            os.mkdir(lable)
        #直接打开文件，如果不存在文件，会创建，将内容写入到文件中
        with open(lable + '/' + str(filename) + '.txt', 'w', encoding='utf-8') as wfile:
            wfile.write(content)

# ArticleId
# ArticleTitle
# ArticleText
# Categorization

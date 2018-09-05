'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/5
@Program      : 将该页面中图片的URL提取出来,并输出所有图像的URL。
'''
#在_____上填写一行代码
#在……上填写一段代码

#读取HTML文件内容，返回一个列表
def getHTMLlines(htmlpath):
    with open(htmlpath,'r',encoding='utf-8') as f:
        data = f.readlines()
    return data

#用于解析文件并提取图像的URL
def extractImageUrls(htmllist):
    urlsList = []
    for item in htmllist:
        if 'img' in item:
            data = item.split('src=')[-1].split('"')[1]
            if 'http' in data:
                urlsList.append(data)
    return urlsList

#将获取的链接输出到屏幕上
def showResults(urls):
    count = 1
    for url in urls:
        print("第{:2}个URL:{}".format(count,url))
        count += 1

# 主程序：1 读取文件；2 解析并提取其中的图片链接；3 输出提取结果到屏幕
def main():
    htmlpath = 'ngchina.html'
    htmldata = getHTMLlines(htmlpath)
    htmllist = extractImageUrls(htmldata)
    showResults(htmllist)

main()

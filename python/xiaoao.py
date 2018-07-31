'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/31
@Program      : 分词统计笑傲江湖的各词出现频率，做成词云
'''
import jieba
import wordcloud

with open('../sample/笑傲江湖-网络版.txt', 'r', encoding='utf-8') as inFile:
    txtData = inFile.read()

wordlist = jieba.lcut(txtData)

cloud = wordcloud.WordCloud(max_words=200, width=1000, height=600)
cloud.generate(' '.join(wordlist))
# cloud.generate_from_frequencies(' '.join(wordlist))
cloud.to_file('xiaoao.png')
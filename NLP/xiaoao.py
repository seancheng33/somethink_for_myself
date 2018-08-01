'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/31
@Program      : 分词统计笑傲江湖的各词出现频率，做成词云，统计出出现的名词和状态词
'''
import jieba
import jieba.analyse
import wordcloud

with open('../sample/笑傲江湖-网络版.txt', 'r', encoding='utf-8') as inFile:
    txtData = inFile.read()

wordlist = jieba.lcut(txtData)

wordcount = jieba.analyse.extract_tags(''.join(wordlist), topK=200, allowPOS=('n'))

print(wordcount)

cloud = wordcloud.WordCloud(font_path='simhei.ttf', max_words=200, width=800, height=600)
cloud.generate(' '.join(wordcount))
# cloud.generate_from_frequencies(' '.join(wordlist))
cloud.to_file('笑傲江湖名词Top200.png')
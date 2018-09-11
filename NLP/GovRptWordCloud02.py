"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/11
@Program      : 词云基础练习,政府报告词云
"""
import jieba
import wordcloud
from scipy.misc import imread

mask = imread('fivestart.png')
with open('关于实施乡村振兴战略的意见.txt', 'r', encoding='utf-8') as f:
    t = f.read()

ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700, background_color='white',mask=mask)
w.generate(txt)
w.to_file('grwordcloud03.png')

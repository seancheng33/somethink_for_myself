"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/11
@Program      : 词云基础练习
"""
import wordcloud

txt = "life is short,you need python"
w = wordcloud.WordCloud(background_color='white')
w.generate(txt)
w.to_file('pywcloud.png')

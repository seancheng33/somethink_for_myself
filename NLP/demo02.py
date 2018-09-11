"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/11
@Program      : 词云基础练习,中文
"""
import jieba
import wordcloud

txt = "程序设计语言用于书写计算机程序的语言。语言的基础是一组记号和一组规则。根据规则由记号构成的记号串的总体就是语言。\
在程序设计语言中，这些记号串就是程序。程序设计语言有3个方面的因素，即语法、语义和语用。语法表示程序的结构或形式，\
亦即表示构成语言的各个记号之间的组合规律，但不涉及这些记号的特定含义，也不涉及使用者。语义表示程序的含义，\
亦即表示按照各种方法所表示的各个记号的特定含义，但不涉及使用者。"
w = wordcloud.WordCloud(width=1000, height=700, font_path='msyh.ttc')
w.generate(' '.join(jieba.lcut(txt)))
w.to_file('pywcloud02.png')

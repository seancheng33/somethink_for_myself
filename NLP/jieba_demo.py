'''
jieba分词的练习，或者是词频的统计练习
'''
from collections import Counter
import jieba
import jieba.analyse

# with open('sample/余罪完整+精校版.txt', 'r', encoding='utf-8') as txt_file:
with open('sample/摸金校尉之九幽将军.txt', 'r', encoding='utf-8') as txt_file:
    # 读取一本小说，用来做分析用
    text_data = txt_file.read().replace('\n','').strip()
'''
#不要一行一行的弄，还是这个文章弄了，再统计比较省事，这个一行行的这个，目前还没有想到适用的场景。
# seg_list = []
#
# for data_line in text_data:
#     text_line = data_line.replace('\n', '').replace('\r', '').strip()  # 先读取每行数字，清理掉换行符和空格
#     seg = jieba.cut(text_line)  # 分词
#     seg_list.append(','.join(seg))
'''
seg_list = jieba.cut(text_data) # 分词



# with open('dict.txt', 'w', encoding='utf-8') as wf:
#     # 分词结果保存至一个文件中
#     wf.write(''.join(seg_list))

# keywords = jieba.analyse.extract_tags(''.join(seg_list), topK=20, withWeight=True)  # 查找词频高的20项内容,且显示权重
# keywords = jieba.analyse.textrank(''.join(seg_list), topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))  # 查找词频高的20项内容
# for word in keywords:
#     print(word)


count = Counter(seg_list) # 统计词频
print(count)

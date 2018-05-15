'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/15

提取文本数据的词干

三种词干提取算法，Lancaster词干提取器比其他两个词干提取器更严格
严格程度而言：Porter最轻松，Lancaster最严格。
Lancaster速度快但是会减少单词的很大部分，通常会选择Snowball词干提取器
'''
from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer

words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'grounded', 'dreamt', 'envision']

stemmers = ['PORTER', 'LANCASTER', 'SNOWBALL']

stemmer_porter = PorterStemmer()
stemmer_lancaster = LancasterStemmer()
stemmer_snowball = SnowballStemmer('english')

formatted_row = '{:>16}' * (len(stemmers) + 1)
print(formatted_row.format('WORD', *stemmers))

for word in words:
    stemmed_words = [stemmer_porter.stem(word),stemmer_lancaster.stem(word),stemmer_snowball.stem(word)]
    print(formatted_row.format(word, *stemmed_words))

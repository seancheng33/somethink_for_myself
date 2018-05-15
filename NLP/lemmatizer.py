'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/15

词性还原

'''
from nltk import WordNetLemmatizer

words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'grounded', 'dreamt', 'envision']

lemmatizers = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']

lemmatizer_wordnet = WordNetLemmatizer()

formatted_row = '{:24}' * (len(lemmatizers)+1)
print(formatted_row.format('WORD', *lemmatizers))

for word in words:
    lemmatizer_word = [lemmatizer_wordnet.lemmatize(word, pos='n'), lemmatizer_wordnet.lemmatize(word, pos='v')]
    print(formatted_row.format(word, *lemmatizer_word))
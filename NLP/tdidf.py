'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/15
文本分类器
'''
from sklearn.naive_bayes import MultinomialNB

'''
# ssl的这段内容，是解决mac下要下载数据集报ssl错误用的，不是必须的内容
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
'''


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

category_map = {'misc.forsale': 'Sales', 'rec.motorcycles': 'Motorcycles',
                'rec.sport.baseball': 'Baseball', 'sci.crypt': 'Cryptography',
                'sci.space': 'Space'}

training_data = fetch_20newsgroups(subset='train', categories=category_map.keys(), shuffle=True, random_state=7)

vectorizer = CountVectorizer()
X_train_termcounts = vectorizer.fit_transform(training_data.data)
print('Dimensions of training data:', X_train_termcounts.shape)

input_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads'
]

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_termcounts)

classifier = MultinomialNB().fit(X_train_tfidf, training_data.target)

X_input_termcounts = vectorizer.transform(input_data)

X_input_tfdif = tfidf_transformer.transform(X_input_termcounts)

predicted_categories = classifier.predict(X_input_tfdif)

for sentence, category, in zip(input_data, predicted_categories):
    print('Input:', sentence)
    print('Predicted category:', category_map[training_data.target_names[category]])

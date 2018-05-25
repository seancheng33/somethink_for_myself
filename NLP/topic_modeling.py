'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/25 
'''
from gensim import corpora, models
from nltk import RegexpTokenizer, SnowballStemmer
from nltk.corpus import stopwords


def load_data(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            data.append(line[:-1])

    return data


class Preprocessor(object):

    def __init__(self):
        self.tokenizer = RegexpTokenizer('\w+')
        self.stop_words_english = stopwords.words('english')
        self.stemmer = SnowballStemmer('english')

    def process(self, input_text):
        tokens = self.tokenizer.tokenize(input_text.lower())
        tokens_stopwords = [x for x in tokens if not x in self.stop_words_english]
        tokens_stemmed = [self.stemmer.stem(x) for x in tokens_stopwords]

        return tokens_stemmed


if __name__ == '__main__':

    input_file = 'data_topic_modeling.txt'
    data = load_data(input_file)

    preprocessor = Preprocessor()

    processed_tokens = [preprocessor.process(x) for x in data]

    dict_tokens = corpora.Dictionary(processed_tokens)
    corpus = [dict_tokens.doc2bow(text) for text in processed_tokens]

    num_topic = 2
    num_words = 4

    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=num_topic, id2word=dict_tokens, passes=25)

    print('Most contributing words to the topics:')
    for item in ldamodel.print_topics(num_topics=num_topic, num_words=num_words):
        print('Topic', item[0], '==>', item[1])

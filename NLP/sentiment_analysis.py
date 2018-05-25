'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/17 
'''
import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier


def extract_features(word_list):
    return dict([(word, True) for word in word_list])


if __name__ == '__main__':
    positive_fileids = movie_reviews.fileids('pos')
    negative_fileids = movie_reviews.fileids('neg')

    features_positive = [(extract_features(movie_reviews.words(fileids=[f])), 'Positive') for f in positive_fileids]
    features_negative = [(extract_features(movie_reviews.words(fileids=[f])), 'Negative') for f in negative_fileids]

    threshold_factor = 0.8
    threshold_positive = int(threshold_factor * len(features_positive))
    threshole_negative = int(threshold_factor * len(features_negative))

    features_train = features_positive[:threshold_positive] + features_negative[:threshole_negative]
    features_test = features_positive[threshold_positive:] + features_negative[threshole_negative:]

    print('Number of training datapoints:', len(features_train))
    print('Number of test datapoints:', len(features_test))

    classifier = NaiveBayesClassifier.train(features_train)
    print('Accuracy of the classifier:', nltk.classify.util.accuracy(classifier, features_test))

    print('Top 10 most informative words')
    for item in classifier.most_informative_features()[:10]:
        print(item[0])

    input_reviews = [
        "It is an amazing movie",
        "This is a dull movie. I would never recommend it to anyone",
        "The cinematography is pretty great in this movie",
        "The direction was terrible and the story was all over the place"
    ]

    print('Predictions:')
    for review in input_reviews:
        print('Review:', review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()

        print('Predicted sentiment:', pred_sentiment)
        print('Probability:', round(probdist.prob(pred_sentiment), 2))

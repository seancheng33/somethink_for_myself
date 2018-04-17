import json
import numpy as np

from pearson_score import pearson_score


def generate_recommendations(dataset,user):
    if user not in dataset:
        raise TypeError('User' + user + ' not present in  the dataset')

    total_scores = {}
    similarty_sums = {}

    for u in [x for x in dataset if x!=user]:
        similarty_score = pearson_score(dataset,user,u)

        if similarty_score<=0:
            continue

        for item in [x for x in dataset[u] if x not in dataset[user] or dataset[user][x] == 0]:
            total_scores.update({item:dataset[u][item]*similarty_score})
            similarty_sums.update({item:similarty_score})

    if len(total_scores) == 0:
        return ['No recommendations possible']

    movie_ranks = np.array([[total/similarty_sums[item],item] for item, total in total_scores.items()])

    movie_ranks = movie_ranks[np.argsort(movie_ranks[:,0])[::-1]]

    recommendations = [movie for _, movie in movie_ranks]

    return recommendations

if __name__ == '__main__':
    data_file = 'movie_ratings.json'
    with open(data_file,'r') as f:
        data = json.loads(f.read())

    user = 'Michael Henry'
    print('Recommendations for '+ user+' : ')
    movies = generate_recommendations(data,user)
    for i, movie in enumerate(movies):
        print(str(i+1)+'. '+movie)
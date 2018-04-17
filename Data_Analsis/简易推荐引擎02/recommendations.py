'''
利用MovieLens数据集，练习制作一个推荐引擎，利用皮尔逊相关系数计算出和其他用户的分数生产推荐列表
数据文件中，用户名是字符串的1-943，电影是字符串的1-1682，8万条评分，评分等级是满分5分
'''
import numpy as np


# 计算数据集中两个用户的皮尔逊相关系数
def pearson_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('User ' + user1 + ' not present in the dataset')
    if user2 not in dataset:
        raise TypeError('User ' + user2 + ' not present in the dataset')

    rated_by_both = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            rated_by_both[item] = 1

    num_ratings = len(rated_by_both)

    if num_ratings == 0:
        return 0

    user1_sum = np.sum([dataset[user1][item] for item in rated_by_both])
    user2_sum = np.sum([dataset[user2][item] for item in rated_by_both])

    user1_square_sum = np.sum([np.square(dataset[user1][item]) for item in rated_by_both])
    user2_square_sum = np.sum([np.square(dataset[user2][item]) for item in rated_by_both])

    product_sum = np.sum([dataset[user1][item] * dataset[user2][item] for item in rated_by_both])

    sxy = product_sum - (user1_sum * user2_sum / num_ratings)
    sxx = user1_square_sum - np.square(user1_sum) / num_ratings
    syy = user2_square_sum - np.square(user2_sum) / num_ratings

    if sxx * syy == 0:
        return 0

    return sxy / np.sqrt(sxx * syy)


def generate_recommendations(dataset,user):
    if user not in dataset:
        raise TypeError('User ' + user + ' not present in the dataset')

    total_scores ={}
    similarity_sums = {}

    for u in [x for x in dataset if x!=user]:
        similarity_score = pearson_score(dataset,user,u)

        if similarity_score <= 0:
            continue

        for item in [x for x in dataset[u] if x not in dataset[user] or dataset[user][x] == 0]:
            total_scores.update({item:dataset[u][item]*similarity_score})
            similarity_sums.update({item:similarity_score})

        if len(total_scores) == 0:
            return ['No recommendations possible']
    movie_ranks = np.array([[total/similarity_sums[item],item] for item, total in total_scores.items()])
    movie_ranks = movie_ranks[np.argsort(movie_ranks[:,0])[::-1]]

    recommendations = [movie for _, movie in movie_ranks]

    return recommendations


if __name__ == '__main__':
    # 数据预处理
    filename = 'sample/u1.base'
    dataset = []
    with open(filename, 'r') as f:
        datas = f.readlines()

        for data in datas:
            dataline = data.split('\t')[:-1]
            dataset.append(dataline)

    # 将数据组合成一个数据字典，大致的格式为{用户名：{电影名：评分，电影名：评分}，用户名：{电影名：评分，电影名：评分}}
    # 方便后面处理
    data_dict = {}
    for name, movie, rating in dataset:
        if name not in data_dict:
            data_dict[name] = {}
        data_dict[name][movie] = int(rating)  # 读过来的数据，这里是字符串，需要转成int，因为后面要计算值

    # print(data_dict)

    # u1 = '100'
    # u2 = '400'
    #
    # print(pearson_score(data_dict, u1, u2))

    user = '500'
    movies = generate_recommendations(data_dict, user)
    for i, movie in enumerate(movies[:10]):  # 只取排名前十的推荐
        print(str(i+1), movie)

    # print(len(movies))

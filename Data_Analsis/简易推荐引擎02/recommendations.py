'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 2018年4月17日
利用MovieLens数据集，练习制作一个推荐引擎，利用皮尔逊相关系数计算出和其他用户的分数生产推荐列表
数据文件中，用户名是字符串的1-943，电影是字符串的1-1682，8万条评分，评分等级是满分5分
'''
import numpy as np


# 计算数据集中两个用户的皮尔逊相关系数
def pearson_score(dataset, user_a, user_b):
    if user_a not in dataset:
        raise TypeError('用户', user_a, '不在数据集中')
    if user_b not in dataset:
        raise TypeError('用户', user_b, '不在数据集中')

    rated_by_both = {}
    for item in dataset[user_a]:
        if item in dataset[user_b]:
            rated_by_both[item] = 1

    num_ratings = len(rated_by_both)

    if num_ratings == 0:
        return 0

    user_a_sum = np.sum([dataset[user_a][item] for item in rated_by_both])
    user_b_sum = np.sum([dataset[user_b][item] for item in rated_by_both])

    user_a_square_sum = np.sum([np.square(dataset[user_a][item]) for item in rated_by_both])
    user_b_square_sum = np.sum([np.square(dataset[user_b][item]) for item in rated_by_both])

    product_sum = np.sum([dataset[user_a][item] * dataset[user_b][item] for item in rated_by_both])

    sxy = product_sum - (user_a_sum * user_b_sum / num_ratings)
    sxx = user_a_square_sum - np.square(user_a_sum) / num_ratings
    syy = user_b_square_sum - np.square(user_b_sum) / num_ratings

    if sxx * syy == 0:
        return 0

    return sxy / np.sqrt(sxx * syy)

# 根据用户，遍历全部的用户，计算皮尔逊相关系数，将符合条件的电影加入到推荐列表中。
def generate_recommendations(dataset, user):
    if user not in dataset:
        raise TypeError('用户', user, '不在数据集中')

    total_scores = {}
    similarity_sums = {}

    for u in [x for x in dataset if x != user]:
        similarity_score = pearson_score(dataset, user, u)

        if similarity_score <= 0.9:
            # 用户量大，有近千用户，如果取相似度大于0的，可能将全部的电影内容都推荐出来。这样的推荐就没有意义。
            # 如果用户的相似度低于0.9的推荐不要，要找相似度高的用户的共同数据推荐才有意义
            continue

        for item in [x for x in dataset[u] if x not in dataset[user] or dataset[user][x] == 0]:
            total_scores.update({item: dataset[u][item] * similarity_score})
            similarity_sums.update({item: similarity_score})

        if len(total_scores) == 0:
            return ['没有可推荐内容，或用户关联度低，无法推荐']
    movie_ranks = np.array([[total / similarity_sums[item], item] for item, total in total_scores.items()])
    movie_ranks = movie_ranks[np.argsort(movie_ranks[:, 0])[::-1]]  # 降序排序，这样就是按分数高到低排序，后面可以只取分数的的几位显示

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
    # 方便后面处理数据，取值、计算
    data_dict = {}
    for name, movie, rating in dataset:
        if name not in data_dict:
            data_dict[name] = {}
        data_dict[name][movie] = int(rating)  # 读过来的数据，这里是字符串，需要转成int，因为后面要计算值

    # print(data_dict)

    # 两个用户的皮尔逊相关系数，从-1到1之间
    # u1 = '10'
    # u2 = '940'
    #
    # print(pearson_score(data_dict, u1, u2))

    user = '660'
    movies = generate_recommendations(data_dict, user)
    print('用户'+user+'可以推荐的总电影条数：', len(movies))
    print('以下为前十条推荐')
    for i, movie in enumerate(movies[:10]):  # [:10]只取排名前十的推荐
        print('第'+str(i + 1)+'条推荐：', movie)



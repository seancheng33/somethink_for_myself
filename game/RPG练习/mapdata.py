'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 2018/6/15 
@Program  : 地图配置文件
'''

# 角色的初始位置
role_postion = {'base': (10, 12),
                'sea': (0, 0)
                }
# 地图的入口和出口 可以有多个，比如一个城市的出入口可以是出入到大地图、各种商店、隐藏剧情的房子等等，一个字典中包含多个字典来控制
inter_postion = {'base': {'tosea': (10, 10), 'itemshop': (5, 5), 'bank': (15, 20)},
                 'sea': {'tobase': (5, 5)}
                 }

# 基本主地图
mapBase = [
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'c', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'l', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', '*', '*', '*', '*', '*', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', '*', 'g', 'g', '*', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', '*', 'g', '*', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', '*', 'g', '*', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', '*', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
     'g', 'g', 'g', 'g', 'g', 'g']
]

# 一个全是水的小地图
mapSea = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 's', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
          ]

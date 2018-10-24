'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/23
@program: pandas的dataframe练习，将一段list格式的数据转换为dataframe的格式
'''
import pandas as pd

music_data = [("the rolling stones","Satisfaction"),
              ("Beatles","Let It Be"),
              ("Guns N' Roses","Don't Cry"),
              ("Metallica","Nothing Else Matters")]

singer_list = []
song_list = []

for singer,song_name in music_data:
    singer_list.append(singer)
    song_list.append(song_name)

final_data = pd.DataFrame({'singer':singer_list,'song_name':song_list})

print(final_data)

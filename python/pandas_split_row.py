'''
@Author : sean cheng
@Email  : aya234@163.com
@CreateTime   : 2018/10/25
@program: 文件中有一列需要被分割，且期望的分割是原来的行的其他内容也被一起填充为新的行里面，
直接使用pandas的dataframe来进行处理，代码量其实很少。
'''

import pandas as pd

df = pd.DataFrame(pd.read_csv('/Users/sean/Desktop/内容-新闻.csv'))  #读csv文件为dataframe
new_df = df.drop('封面图片路径',axis=1).join(df['封面图片路径'].str.split('|',
                expand=True).stack().reset_index(level=1))
#new_df.to_csv('/Users/sean/Desktop/内容-新闻_out.csv')  #将处理后的文件保存为csv文件
new_df.to_excel('/Users/sean/Desktop/内容-新闻_out.xlsx')  #将处理后的文件保存为csv文件

'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/8
@Program      : pyplot图
'''
import pandas as pd
import matplotlib.pyplot as plt

lista = [3.04, 22.93, 12.75, 22.6, 12.33]
listb = [8.18, 18.38, 9.13, 7.82, 6.69]
timelist = ['2008', '2009', '2010', '2011', '2012']
plt.plot(timelist, lista, 'ro-', timelist, listb, 'bo-')
plt.title('matplotlib图的练习', fontproperties='SimHei', fontsize=18)
plt.xlabel('2008-2012', fontproperties='SimHei', fontsize=18)
plt.show()

hprice = pd.Series(lista, index=['2008', '2009', '2010', '2011', '2012'])
m2 = pd.Series(listb, index=['2008', '2009', '2010', '2011', '2012'])
print(hprice.corr(m2))

'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/7/2 
@Program       : random函数的shuffle练习,内容为模拟扑克洗牌，先生成52张花色的牌，然后在将他们的顺序打乱
'''
import random

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
num2 = ['♠︎', '♥︎', '♣︎', '♦︎']

poker = []
for i in num2:
    for j in num:
        poker.append(i + j)

print(poker)

random.shuffle(poker)

print(poker)

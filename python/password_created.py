'''
一个密码生产器，根据指定的长度生产密码
'''

import random


seed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+'

pw = []

pw_num = input('输入一个数字作为密码的长度：')

# 方法一
#
# for i in range(int(pw_num)):
#     pw.append(random.choice(seed))
#
# print(''.join(pw))


# 方法二

pw = random.sample(seed,int(pw_num))
print(''.join(pw))

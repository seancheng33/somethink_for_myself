'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）生成随机密码
'''
import random

random.seed(0x1010)

s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

rdPass = []

while len(rdPass) < 10:
    password = random.choices(s,10)

    rdPass.append(password)

print(rdPass)

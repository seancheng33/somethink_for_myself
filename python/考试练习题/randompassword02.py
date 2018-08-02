'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/30
@Program      : （考试练习题）生成一组10个随机密码，每个没密码长度10
'''
import random

random.seed(0x1010)

s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

rdPass = []
checkPass = ''
while len(rdPass) < 10:
    password = random.sample(s,10)
    
    if password[0] in checkPass:
        continue
    else:
        checkPass += password[0]
        rdPass.append(''.join(password))
print(rdPass)
with open('随机密码2.txt','w') as passFile:
    passFile.write('\n'.join(rdPass))

'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/7/31
@Program      : 移位10451位的中文凯撒密码
'''
s= input('输入（加解密前）：')

d = {}
for i in [0x4e00,0x9fa]:
    for c in range(20902):
        d[chr(i+c)] = chr((i+10451) % 20902 + c)
print('输出（加解密后）：'+''.join([d.get(c,c) for c in s]))

"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/11
@Program      : 基础的文件控制的练习，将一个列表写入文件，
				然后重新将指针返回到文件的开始位置，读取文件
"""
ls = ['中国','法国','英国','美国']
with open('output.txt','w+') as fo:
    fo.writelines(ls)
    fo.seek(0)
    for line in fo:
        print(line)
'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/16
@Program      : 华氏与摄氏温度转换,简单基础练习
'''

val = input("输入你要需要转换的温度及单位（如：32C 或 100F）：")

if val[-1] in ('C','c'):
	f = float(val[0:-1]) * 1.8 + 32
	print("你输入的温度是{}℃，转换为{} ℉".format(val[0:-1],round(f,2))) 
elif val[-1] in ('F','f'):
	c = (float(val[0:-1])-32)/1.8
	print("你输入的温度是{}℉，转换为{} ℃".format(val[0:-1],round(c,2))) 
else:
	print("输入有误！")

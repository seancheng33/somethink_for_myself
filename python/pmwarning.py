'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/16
@Program      : 基础练习，空气质量的判断
'''

def main():
	PM = eval(input("What is today's PM2.5?"))
	if PM > 75:
		print('Unhealthy. Be careful!')
	if PM < 35:
		print("Good. Go running!")

main()
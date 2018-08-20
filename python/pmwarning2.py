'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/16
@Program      : 基础练习，空气质量的判断
'''

def main():
	PM = eval(input("What is today's PM2.5?"))
	if PM > 250:
		print('Hazardous. REMAIN INDOORS!')
	elif PM > 150:
		print('Very unhealthy. Avoid prolonged exertion!')
	elif PM > 115:
		print('Unhealthy. Limit prolonged exertion!')
	elif PM > 75:
		print('Unhealthy for sensitive group!')
	elif PM > 35:
		print('Unhealthy. Be careful!')
	else:
		print("Good. Go running!")

main()

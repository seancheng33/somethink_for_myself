'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/30
@Program      : python基础练习题，EAN-13的校验码计算
'''

strNum = '697145891104'
indexNum = 0
num1 = 0
num2 = 0
for i in strNum:
	if indexNum % 2 == 0:
		num1 += eval(i)
	else:
		num2 += 3 * eval(i)
	indexNum += 1
total = num1 + num2
result = total % 10
if result == 0 :
	print(0)
else:
    print(10 - result)


'''
6971458911047
6901234567892
6922266443770
'''

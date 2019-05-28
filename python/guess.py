import random

finalNum = random.randint(0,100)

while True:
    num = eval(input("请输入一个1-100的数字："))
    
    if num > finalNum:
        print("你输入的数字比要猜的数字大")
    elif num < finalNum:
        print("你输入的数字比要猜的数字小")
    elif num == finalNum:
        print("恭喜你猜中了")
        break
    else:
        print("输入有误，请重新输入")

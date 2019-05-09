#!/bin/bash
# 猜数字的游戏，利用秒数生成随机数。
#
guessNum=`date|cut -nb 25-26`

while : 
do
read -p "请输入一个0-59之间的数字(输入q退出游戏)：" num
if [ $num = q ]
then
 break
fi

if [ $num -lt $guessNum ]
then
    echo "你输入的数字比要才的数字小"
elif [ $num -gt $guessNum ]
then
    echo "你输入的数字比要猜的数字大"
elif [ $num -eq $guessNum ]
then
    echo "恭喜你猜中了"
    break
else
    echo "输入有误，请重新输入"
fi
done
  

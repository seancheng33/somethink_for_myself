#!/bin/bash

echo "欢迎来到石头剪刀布游戏,(0=剪刀,1=石头,2=布),输入q退出游戏："
while :
do
    num=$[$RANDOM%3]
    read -p "Please input a num:" p
    case "$p" in
    0)
    if [ $num -eq 0 ]
    then
        echo "平局"
    elif [ $num -eq 1 ]
    then
        echo "你输了"
    else
        echo "你赢了"
    fi;;
    1)
    if [ $num -eq 1 ]
    then
        echo "平局"
    elif [ $num -eq 0 ]
    then
        echo "你赢了"
    else
        echo "你输了"
    fi;;
    2)
    if [ $num -eq 2 ]
    then
        echo "平局"
    elif [ $num -eq 1 ]
    then
        echo "你输了"
     else
        echo "你赢了"
    fi;;
    q|Q)
        exit;;
    *)
        echo "输入无效。0=剪刀,1=石头,2=布，q或Q=退出";;
    esac
done

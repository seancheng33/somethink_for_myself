#!/bin/bash

# final_num=`date +%s|md5sum|tr -d [a-f]|cut -b -2`
# echo $final_num

# while read -n2 -p "input a number 0-99：" input_num
# do
#     echo
#     if [ $input_num -gt $final_num ]
#     then
#         echo "你猜大了"
#         continue
#     elif [ $input_num -lt $final_num ]
#     then
#         echo "你猜小了"
#         continue
#     elif [ $input_num -eq $final_num ]
#     then
#         echo "你猜对了"
#         exit
#     fi
# done


final_num=`date +%s|md5sum|tr -d [a-f]|cut -b -2`
echo "$final_num"

shangxian=100
xiaxian=0
zhongjian=$[ $shangxian / 2 ]

until [ $zhongjian -eq $final_num ]
do  
    echo "猜$zhongjian"
    if [ $zhongjian -gt $final_num ]
    then
        shangxian=$zhongjian
    elif [ $zhongjian -lt $final_num ]
    then
        xiaxian=$zhongjian
    fi
    zhongjian=$[ $[$shangxian + $xiaxian] / 2 ]
done
echo "你猜对了,就是$zhongjian"

#! /bin/bash
# 根据用户输入的数字，输出对应数组的等边三角形。
read -p "Please Enter a number:" Line

for ((i=1;i<Line;i++))
do
  for ((j=$Line-$i;j>0;j--))
  do
    echo -n ' '
  done
  for ((h=1;h<=$((2*$i-1)); h++))
  do
    echo -n '*'
  done
  echo
done

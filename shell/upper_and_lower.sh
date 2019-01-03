#!/bin/bash
#修改文件夹及其子文件夹里面的文件和文件夹的名字大小写
#使用方式：
#1. tr '[A-Z]' '[a-z]'：大写改小写，如果倒过来tr '[a-z]' '[A-Z]'：就是小写改大写
#2. if [ -d "$1" ]; then 的作用是判断值是否文件夹，如果执行这个判断，就只修改文件夹的大小写；
#如果不执行这个就是修改文件夹及文件的大小写，连后缀名都会被修改。
#3. 执行方式是./upper_and_lower.sh 父级的文件路径
#./upper_and_lower.sh ./转换目录
#./upper_and_lower.sh ./文件名称

cvitem() 
{
  DName=`dirname $1`
  BName=`basename $1`
  lc_BName=`basename $1 | tr '[A-Z]' '[a-z]'`
  if [ "$BName" = "$lc_BName" ]; then
    echo "****: $1 ---x--- $DName/$lc_BName identical!"
  else
    if [ -d "$1" ]; then
    echo "----renaming $1 to $DName/$lc_BName ..."
    mv $1 $DName/$lc_BName
    fi
  fi
}
 
[ $# = 0 ] && { echo "Usage: lcdir item1 item2 ..."; exit; }
 
for item in $*
do
  [ "`dirname $item`" != "`basename $item`" ] && {
  [ -d $item ] &&
  {
  for subitem in `ls $item`
  do
  ./upper_and_lower $item/$subitem
  done
  }
  cvitem $item
}
done

#!/bin/bash
#
# 批量修改文件后缀名及文件名大小写
#

cd /tmp

for i in `seq 50`
do
    mktemp XXXXXX.tmp
done

# 修改文件后缀名
for filename in `ls *.tmp`
do 
    refilename=`basename $filename|tr '.tmp' '.log'`
    mv $filename  $refilename
done

# 修改文件名的大小写
for filename in `ls *.log`
do 
    # refilename=`basename $filename|tr 'A-Z' 'a-z'`    # 大写改小写
    refilename=`basename $filename|tr 'a-z' 'A-Z'`      # 小写改大写
    
    mv $filename  $refilename
done

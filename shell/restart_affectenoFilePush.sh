#!/bin/sh

ID=`ps -ef | grep "AffectenoFilePush" | grep -v "grep" | awk '{print $2}'`  
echo $ID  
echo "---------------"  
for id in $ID  
do  
kill -9 $id  
echo "killed $id"  
done
nohup sh /home/sczx/do1/stmsapp/bin/affectenoFilePush.sh run > /home/sczx/do1/stmsapp/bin/affectenoFilePush.log &
echo "AffectenoFilePush restart"

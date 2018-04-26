#!/bin/sh

ID=`ps -ef | grep "tomcat" | grep -v "grep" | awk '{print $2}'`  
echo $ID  
echo "---------------"  
for id in $ID  
do  
kill -9 $id  
echo "killed $id"  
done  
sh /home/sczx/do1/apache-tomcat-6.0.44/bin/startup.sh
echo "Tomcat restart"

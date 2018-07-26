#!/bin/sh

ID=`ps -ef | grep "node1" | grep -v "grep" | awk '{print $2}'`  
echo $ID  
echo "---------------"  
for id in $ID  
do  
kill -9 $id  
echo "killed $id"  
done
rm -rf /home/stvasms/mcs/ActiveMQ4.1.2/node1/activemq-data/kaha.db
nohup sh /home/stvasms/mcs/ActiveMQ4.1.2/node1/bin/activemq &

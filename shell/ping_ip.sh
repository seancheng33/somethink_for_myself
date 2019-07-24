#!/bin/bash

# read -p "请输入需要检测的ip段（例如：192.168.210.）:" ipa;

up=0
down=0

for ipaddr in {1..254}
do
    # echo $ipa$ipaddr
    if `ping -c 2 -t 1 -w 1 192.168.210.$ipaddr|grep -q time=`
    then
        up=$[$up + 1]
        # echo "up $up"
        echo "$ipa$ipaddr is UP!" >> up.txt 2>&1
    else
        down=$[$down + 1]
        # echo "down $down"
        echo "$ipa$ipaddr is DOWN!" >> down.txt 2>&1
    fi
done

echo "在线ip数量 $up ;离线ip数量 $down ."
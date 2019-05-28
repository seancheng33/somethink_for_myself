#!/bin/bash

eth=$1
config_path=/etc/sysconfig/network-scripts/ifcfg-$eth
# 先启动网卡，利用dhcp获取到IP等各项信息，休眠10秒只是为了等待dhcp的完成
ifup $eth
sleep 10

# 通过ifconfig命令和route命令获取到对应的ip netmask和gateway
ipaddress=`ifconfig $eth|grep inet|head -1|awk '{print $2}'`
netmask=`ifconfig $eth|grep inet|head -1|awk '{print $4}'`
gateway=`route -n|sed -n '/'$eth'/ p'|awk '{print $2}'|head -1`

# 获取当前时间秒数，用于备份文件时作为标识
current_time=`date +"%s"`
# 先将配置文件备份
cp $config_path $config_path.bak$current_time

# 利用sed命令去替代和追加对应的项。
sed -i 's/ONBOOT=no/ONBOOT=yes/' $config_path
sed -i 's/BOOTPROTO=dhcp/BOOTPROTO=static/' $config_path
sed -i '$a IPADDR='$ipaddress $config_path
sed -i '$a NETMASK='$netmask $config_path
sed -i '$a GATEWAY='$gateway $config_path

echo "nameserver 114.114.114.114" >> /etc/resolv.conf

# 重启网络服务
systemctl restart network

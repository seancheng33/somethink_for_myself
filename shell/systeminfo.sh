#!/bin/bash
#
# 检测一组服务器的cpu核心数和内存数，同时查看/data是否存在且有磁盘或分区挂载
# 基于sshpass来对各台服务器进行用户名及密码的连接。首先先确保可以安装

# 以下的内容为需要检查的各服务器的ip放在双引号里面，用空格分隔
host=("192.168.18.10" "192.168.18.90")
# ssh的用户名
username="root"
# ssh的密码
password="123456"
# ssh的端口号
sshport=22

# 检查执行脚本的服务器有没有安装sshpass包
if rpm -q sshpass &>/dev/null
then
    echo "sshpass已经存在，无需安装"
else
    # 如果同目录里面有sshpass的包，就安装，没有则给出提示
	if [ -f "sshpass-1.06-2.el7.x86_64.rpm" ]
	then
        rpm -ivh sshpass-1.06-2.el7.x86_64.rpm
	else
		echo "sshpass包不存在，请确认该rpm包在脚本的目录里面"
		echo "如果服务器支持yum安装，可以执行“yum install sshpass”后再执行本脚本"
		exit
	fi
fi

# 循环执行，获取host数组里面的各服务器的信息
for ip in ${host[*]}
do
   echo "==== $ip 的CPU核心数 ===="
   sshpass -p $password ssh root@$ip -p $sshport cat /proc/cpuinfo|grep "core id"|wc -l
   echo "==== $ip 的内存总量(单位：m) ===="
   sshpass -p $password ssh root@$ip -p $sshport free -m|awk '{if(NR==2) print $2}'
   echo "==== $ip 查看/data是否存在且有磁盘或分区挂载 ===="
   sshpass -p $password ssh root@$ip -p $sshport  ls -d /data|wc -c|awk '{if($1>0){print "该目录已存在"}else{print "没有该目录"}}'
   sshpass -p $password ssh root@$ip -p $sshport df -h|sed -n "/\/data/p"|wc -l|awk '$1==1{print "有磁盘或分区挂载在/data"} $1==0{print "没有磁盘或分区挂载在/data"}'
done

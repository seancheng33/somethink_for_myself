#!/bin/bash
# 基于安全的考虑，查询企图暴力破解登录的IP,将这些IP添加到/etc/hosts.deny里面。
# 如果该IP出现在登录失败的列表中次数超过5次，就会被添加到文件中。
# 将此脚本添加到周期定时任务中，以此实现每分钟检查一次数据。


# 查询登录失败的资料，并将其保持为一个临时文件
# 关于awk里面的if判断，因为在运行时发现，登录失败的情况中包括了一种是使用空的用户名，
# 这种情况下，ip实际是被解析成第二列，需要对行的列数进行判断，确保可以获取到的都是ip，
# 而非其他的信息。即只有行里面是10列和9列才是这些登录失败的信息。
lastb|awk '{if(NF==10) print $3;else if(NF==9) print $2}'|sort -n|uniq -c|sort -nr > /tmp/ip.tmp

# 读取上面存下来的文件里面的内容，以行为单位。每行的内容包括该IP地址和该IP出现多少次的统计
while read line
do
	num=`echo $line|awk '{print $1}'`		# IP出现的次数
	ipaddr=`echo $line|awk '{print $2}'`	# IP地址
	
	# 如果IP出现的次数是小于5次，则不做任何处理，否则，进行添加到文件的相关处理。
	if [ $num -lt 5 ]
	then
		continue
	else
		# 判断该IP是否存在于文件中，如果存在则跳出循环，否则将内容该IP添加到文件中。
		if `grep -q "$ipaddr" /etc/hosts.deny`
		then
			continue
		else
			# 在将IP添加到文件之前，输出一条日志记录，记录了什么时间添加了什么IP到文件中。
	        echo $ipaddr于`date +%F" "%T`被记录到hosts.deny中。 >> /mnt/usbdisk1/PySpider/ipdeny.log
			# 将该IP地址添加到文件中，禁止该IP的访问
			echo "sshd:$ipaddr" >> /etc/hosts.deny
		fi
	fi
done < /tmp/ip.tmp

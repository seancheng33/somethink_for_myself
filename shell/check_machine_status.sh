#! /bin/bash

PS3="输入1-3检查(4:退出):"
select option in "CPU Cores" "Memory" "Disk Mount" "Exit"
do
    case $option in
	"CPU Cores")
	# 查找cpu的核心id，然后统计多少行，达到统计cpu核心数的目的
	    cores=`grep "core id" /proc/cpuinfo|wc -l`
	    echo "当前系统的CPU核心为 $cores 核。"
	;;
	"Memory")
	# 直接查看以M为单位的内存总量
	    men=`free -m|awk '{if(NR==2) print $2}'`
	    echo "当前系统内存总量： $men M。"
	;;
	"Disk Mount")
	# 查看挂载情况，并且查看是否有内容，来判断是否有挂载数据盘
	    mounted=(`df -h|sed -n "/\/data/p"`)
	    
	    # 如果上面的结果数组长度为零，则表示没有挂载 
	    if [ ${#mounted[*]} -eq 0 ] 
	    then
	        echo "没有硬盘分区挂载到/data。"
	    else
		echo "有硬盘分区挂载到/data。"
	    fi
	;;
	"Exit")
	    exit
	;;
	*)
	    echo "输入有误，请重新输入。"
	;;
    esac
done

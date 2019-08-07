#!/bin/bash
# 收集本机一些硬件信息

PS3="Your choice is[8 for quit]: "
select choice in Disk_Info CPU_Info Men_Util System_Info Serial_Number Online_Users Login_Failed Quit
do

  case "$choice" in
    Disk_Info) 
      echo "==========Disk Info=========="
      df -Th |grep -v "tmpfs"  
      ;;
    CPU_Info)
      echo "==========CPU Info=========="
      grep "model name" /proc/cpuinfo
      grep "cpu MHz" /proc/cpuinfo
      cpuload=`uptime|awk -F : '{print $NF}'`
      echo "load average: $cpuload"
      ;;
    Men_Util)
      echo "==========Men Util=========="
      grep "MemTotal" /proc/meminfo
      grep "MemFree" /proc/meminfo
      grep "SwapTotal" /proc/meminfo
      grep "SwapFree" /proc/meminfo
      ;;
    System_Info)
      echo "==========System Info=========="
      hostname
      cat /etc/redhat-release 
      getconf LONG_BIT
      ;;
    Serial_Number)
      echo "==========Serial Number=========="
      dmidecode |grep "Serial Number"|head -1
      ;;
    Online_Users)
      echo "==========Online Users=========="
      who
      ;;
    Login_Failed)
      echo "==========Login Failed=========="
      lastb|head
      ;;
    Quit)
      exit;;
    *)
      echo "Error input must [1-8]."
  esac
done 

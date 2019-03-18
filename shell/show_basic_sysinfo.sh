#! /usr/bin/bash
# 获取一些简单的系统信息
PS3="Your chioce is[5 for quit]:"

select choice in disk_partition filesystem cpu_load men_util quit
do
  case "$choice" in
    disk_partition)
      fdisk -l
      ;;
    filesystem)
      df -h
      ;;
    cup_load)
      uptime
      ;;
    men_util)
      free -m
      ;;
    quit)
      break;;
    *)
      echo "error input"
  esac
done

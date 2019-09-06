#!/bin/bash
# 
# 自动分区磁盘为一个分区，然后使用uuid自动配置到fstab文件中
# 使其开机自动加载并且在配置后测试加载。

read -p "请输设备名，不需输/dev/(例 vdb，sdb)："  part
# 需要一个异常处理，如果输入的设备名不存在，则重新获取输入

# 使用fdisk对于制定的磁盘进行分区
fdisk "/dev/"$part << EOF
n
p



w
EOF

# 格式化文件系统为ext4格式 
mkfs.ext4 "/dev/"$part"1"

# 获取该分区的uuid
disk_uuid=`blkid|awk '/\/dev\/'$part'1/ {print $2}'|tr -d "\""`

# 将uuid追加到fstab的最后面
echo "$disk_uuid /data                   ext4    defaults        0 0" >> /etc/fstab

# 执行配置文件，将配置挂载出来
mount -a

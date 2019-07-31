#!/bin/bash
# 编写脚本实现监控主机挂载点/data磁盘空间,当使用空间超过80％, 
# 将/data目录下大于100k的文件打包为gz格式的压缩文件并转移到/bak_data目录下

diskfree=`df -h|awk '{if($6~/\/boot/)print $5}'|sed  "s/%//"`
if [ $diskfree -ge 80]
then
       find /data -type f -size +100k -exec gzip {} \;
       find /data -name "*.gz" -exec mv {} /bak_data \;
fi

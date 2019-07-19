#!/bin/bash

list=`cut -d ':' -f 4 /etc/passwd|sort -n|uniq -c|sort -nr|head -3|awk '{print $NF}'`

# echo $list

for gid in $list
do
    echo `grep -w $gid /etc/group|cut -d ':' -f 1`
done
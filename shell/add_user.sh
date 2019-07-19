#!/bin/bash

for name in `cat user.txt`
do
    # useradd $name
    # echo "$name is create!"
    userdel -rf $name
    echo "$name is delete!"
done
#!/bin/bash

read -p "please input a username:" name

if who|grep -q $name
then
    echo "$name is online "
else
    echo "$name is not online "
fi
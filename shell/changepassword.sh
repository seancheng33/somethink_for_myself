#!/bin/bash
for name in natasha harry sarah;
do
 echo centos | passwd --stdin $name;
done

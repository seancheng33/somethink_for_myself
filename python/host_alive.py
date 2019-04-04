#!/usr/bin/python3
'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2019/4/4
@Program      : 收集某一网段的IP段下的存活主机。在linux系统下测试成功。可以正常使用。
'''
import os
import sys
import re
import time
import subprocess

lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")

print(time.ctime())

for host in range(1,255):
	ip = '192.168.1.'+str(host)
	pingaling = subprocess.Popen(['ping','-q','-c 2','-r',ip],shell=False,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	print("Testing",ip,)

	while 1:
		pingaling.stdout.flush()
		line=pingaling.stdout.readline()
		if not line:
			break
		igot = re.findall(lifeline,str(line))
		if igot:
			print(report[int(igot[0])])
print(time.ctime())

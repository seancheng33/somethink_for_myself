'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 2018/4/26
在安装有puppet的机器上利用facter命令收集数据
'''

import subprocess
import re

command = 'facter'
show_list = [('fqdn', '主机名'),
             ('domain', '域名'),
             ('uptime', '运行时间'),
             ('operatingsystem', '系统'),
             ('kernelrelease', '内核版本'),
             ('ipaddress', 'IP'),
             ('macaddress', 'MAC'),
             ('memorysize', '内存'),
             ('processors', 'CPU'),
             ('blockdevices', '磁盘'), ]

def handle_command_message(command):
    status,content = subprocess.getstatusoutput(command)
    if status ==0:
        return content
    else:
        return


if __name__ == '__main__':
    result_dict = {}
    result = handle_command_message(command)

    if result:
        for line in result.strip().split('\n'):
            if re.findall('=>',line):
                key, value = line.split('=>',1)
                result_dict[key.strip()] = value.strip()
        for f_k, f_s in show_list:
            if f_k in result_dict:
                print(f_s,':',result_dict[f_k])
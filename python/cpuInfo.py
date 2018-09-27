"""
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/27
@Program       : 利用psutil库获取cpu信息
"""
import psutil

cpu_data = psutil.cpu_times(percpu=True)
print(cpu_data)

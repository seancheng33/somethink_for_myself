'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/8/2
@Program       : 生成qrcode的练习
'''

from MyQR import myqr
import os

myqr.run(
    words="test python make qrcode",
    version=1,
    level='H',
    brightness=1.0,
    colorized=True,
    picture='bg.gif',
    save_name='testCode.gif',
    save_dir=os.getcwd()
)
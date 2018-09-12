'''
@Author        : sean cheng
@Email         : aya234@163.com
@Create_Time   : 2018/9/12
@Program       : 自动安装第三方库的脚本。
'''

import os
libs={'numpy','matplotlib','pillow','sklearn','requests',
      'jieba','beautifulsoup4','wheel','networkx','sympy',
      'pyinstaller','django','flask','werobot','pyqt5','pandas'
      'pyopengl','pypdf2','docopt','pygame'}
try:
    for lib in libs:
        os.system('pip3 install '+ lib)
        print('Successful')
except:
    print('Failed Somehow')

"""
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/17
@Program      : 基础练习。制作tkinter的gui版本的温度转换计算。
"""

import tkinter as tk


# 计算温度转换的函数
def convert_temp():

    # 获取两个输入框的值
    c = temp_c.get()
    f = temp_f.get()
    try:
        if c != '' and f == '':
            temp = float(c) * 1.8 + 32
            varString.set('你输入的温度是 {} ℃，转换结果为{} ℉'.format(c, round(temp, 2)))
            temp_c.set('')
        elif c == '' and f != '':
            temp = (float(f)-32)/1.8
            varString.set('你输入的温度是 {} ℉，转换结果为{} ℃'.format(f, round(temp, 2)))
            temp_f.set('')
        elif c != '' and f != '':
            varString.set('只需输入其中一项即可')
        else:
            varString.set('没有输入')
    except ValueError:
        varString.set('有误！只接受正负整数或小数，其他字符无效')
        temp_c.set('')
        temp_f.set('')


win = tk.Tk()
win.title('温度转换计算器 ver 1.0')

varString = tk.StringVar()
varString.set('')
temp_c = tk.StringVar()
temp_f = tk.StringVar()

tk.Label(win, text='温度转换计算', font=(None,36,"bold")).grid(row=0, column=0, columnspan=2)
entryc = tk.Entry(win, textvariable=temp_c).grid(row=1, column=0, padx=5)
tk.Label(win, text='℃（摄氏）').grid(row=1, column=1)
entryf = tk.Entry(win, textvariable=temp_f).grid(row=2, column=0)
tk.Label(win, text='℉（华氏）').grid(row=2, column=1)
tk.Button(win, text='计算', command=convert_temp).grid(row=1, column=2, rowspan=2)
tk.Label(win, textvariable=varString).grid(row=3, column=0, columnspan=2, padx=5)
win.mainloop()

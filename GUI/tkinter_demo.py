import tkinter as tk


def result():
    var_text.set('000000')



win = tk.Frame()
win.pack()
tk.Label(win, text='Click Add to get the sum or Quit to Exit.').pack(side=tk.TOP)
tk.Button(win, text='Add', command=result).pack(side=tk.LEFT)
tk.Button(win, text='Exit', command=win.quit).pack(side=tk.RIGHT)
var_text = tk.StringVar()
var_text.set('sum')
resultsum = tk.Label(win, textvariable=var_text).pack(side=tk.BOTTOM)
win.mainloop()

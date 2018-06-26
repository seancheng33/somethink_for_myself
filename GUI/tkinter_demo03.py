import tkinter as tk

win = tk.Tk()

tk.Label(win, text='label01').grid(row=0, column=0)
tk.Label(win, text='label02').grid(row=1, column=0)

e1 = tk.Entry(win, textvariable=tk.StringVar()).grid(row=0, column=1, padx=10, pady=5)
e2 = tk.Entry(win, textvariable=tk.StringVar(), show='*').grid(row=1, column=1, padx=10, pady=5)

win.mainloop()

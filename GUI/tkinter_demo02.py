import tkinter as tk


class APP():
    def __init__(self,master):
        win = tk.Frame(master)
        win.pack(side=tk.LEFT,padx=10,pady=10)

        self.button = tk.Button(win,text='button',fg='blue')
        self.button.pack()

root = tk.Tk()
root.title('Tkinter Demo')
# root.geometry((640,480))
app = APP(root)

root.mainloop()
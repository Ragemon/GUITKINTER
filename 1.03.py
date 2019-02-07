##import tkinter as tk
##root = tk.Tk()
##manu_bar = tk.Frame(root)
##label = tk.Label(root, text='My name is courage')
##button = tk.Button(root, text='Click here')
##manu_bar.pack()
##
##tk.Menubutton(manu_bar, text='file').pack()
##
##
##label.pack()
##button.pack()
##
##
##
##root.mainloop()

import tkinter as tk
root = tk.Tk()

def hello():
    print('hello')

menubar = tk.Menu(root)
menubar.add_command(label='Hello!', command=hello)
menubar.add_command(label='Quit', command=root.quit)

root.config(menu=menubar)

root.mainloop()









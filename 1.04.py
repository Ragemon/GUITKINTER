import tkinter as tk
root = tk.Tk()

frame = tk.Frame(root)
# Demo for fill
tk.Label(frame, text= 'Demo for fill').pack()
tk.Button(frame, text='A').pack(side=tk.LEFT, fill=tk.Y)
tk.Button(frame, text='B').pack(side=tk.TOP, fill=tk.X)
tk.Button(frame, text='C').pack(side=tk.RIGHT, fill=tk.NONE)
tk.Button(frame, text='D').pack(side=tk.TOP, fill=tk.BOTH)

frame.pack()

#Demo for expand no fill
tk.Label(root, text='Demo for expand and no fill').pack()
tk.Button(root, text='I do not expand').pack()
tk.Button(root, text='I do not fill x but I expand').pack(expand=4)
tk.Button(root, text='I fill x and expand').pack(fill=tk.X, expand=1)



root.mainloop()

















import tkinter as tk
root = tk.Tk()

root.configure(background='#4D4D4D')# top level styling

# connecting to the external styling optionDB.txt
root.option_readfile('optionDB.txt')

#widget specific styling
mytext = tk.Text(root, background='#101010', foreground='#D6D6D6',borderwidth=18,
             relief='sunken',
             width=17,height=5)

mytext.insert(tk.END,
 'Style is knowing who you are, what you want to say,and not giving a damn.')
mytext.grid(row=0,column=0,columnspan=6,padx=5,pady=5)

## all the below widgets derive their styling from optionDB.txt file

tk.Button(root, text='*').grid(row=1, column=1)
tk.Button(root,text='^').grid(row=1,column=2)
tk.Button(root,text='#').grid(row=1,column=3)
tk.Button(root,text='<').grid(row=2,column=1)
tk.Button(root,text='OK').grid(row=2,column=2)
tk.Button(root,text='>').grid(row=2,column=3)
tk.Button(root,text='+').grid(row=3,column=1)
tk.Button(root,text='v').grid(row=3,column=2)
tk.Button(root,text='-').grid(row=3,column=3)

for i in range(9):
    tk.Button(root,text=str(i+1)).grid(row=4+i//3,column=1+i%3)


root.mainloop()







import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Click at different\nlocations in the frame below').pack()
def callback(event):
    print(dir(event))
    print('You clicked at', event.x, event.y)
    print('You clicked at', event.x_root, event.y_root)

frame = tk.Frame(root, bg='red', width=130, height=80)
frame.bind('<Button-2>', callback)
frame.pack()


root.mainloop()

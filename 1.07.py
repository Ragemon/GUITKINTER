import tkinter as tk

parent = tk.Tk()

parent.title('Find & Replace')

tk.Label(parent, text='Find: ').grid(row=0,column=0, sticky=tk.E)
tk.Entry(parent, width=60).grid(row=0, column=1, padx=2,
                                pady = 2, columnspan=9, sticky=tk.EW)

tk.Label(parent, text='Replace: ').grid(row=1, column=0, padx=2, pady=2,
                                        sticky=tk.E)
tk.Entry(parent).grid(row=1, column=1, padx=2, pady=2, sticky=tk.EW,
                      columnspan=9)

tk.Button(parent, text='Find').grid(row=0, column=10, sticky=tk.E+tk.W, padx=2,
                                        pady=2)
tk.Button(parent, text='Find All').grid(row=1, column=10, sticky=tk.E+tk.W,
                                        padx=2)
tk.Button(parent, text='Replace').grid(row=2, column=10, sticky=tk.E+tk.W,
                                       padx=2)
tk.Button(parent, text='Replace').grid(row=3,column=10, sticky=tk.E+tk.W,
                                       padx=2)

tk.Checkbutton(parent, text='Match whole word only').grid(row=2, column=1,
                                                          columnspan=4,
                                                          sticky=tk.W)
tk.Checkbutton(parent, text='Match Case').grid(row=3, column=1,
                                               columnspan=4,
                                               sticky=tk.W)
tk.Checkbutton(parent, text='Wrap aroun').grid(row=4, column=1,
                                               columnspan=4,
                                               sticky=tk.W)

tk.Label(parent, text='Direction').grid(row=2, column=6, sticky=tk.W)
tk.Radiobutton(parent, text='Up', value=1).grid(row=3, column=6, columnspan=6,
                                                sticky=tk.W)
tk.Radiobutton(parent, text='Down', value=2).grid(row=3,
                                                  column=7, columnspan=2,
                                                  sticky=tk.E)





parent.mainloop()

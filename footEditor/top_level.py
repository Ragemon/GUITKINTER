import tkinter as tk
import tkinter.filedialog,os
root = tk.Tk()
file_name = None
PROGRAM_NAME = ' Footprint Editor '
root.title(PROGRAM_NAME)
root.geometry('350x350')

# getting icons ready for compound menu
new_file_icon = tk.PhotoImage(file='icons/new_file.gif')
open_file_icon = tk.PhotoImage(file='icons/open_file.gif')
save_file_icon = tk.PhotoImage(file='icons/save.gif')
cut_icon = tk.PhotoImage(file='icons/cut.gif')
copy_icon = tk.PhotoImage(file='icons/copy.gif')
paste_icon = tk.PhotoImage(file='icons/paste.gif')
undo_icon = tk.PhotoImage(file='icons/undo.gif')
redo_icon = tk.PhotoImage(file='icons/redo.gif')


menu_bar = tk.Menu(root)




#all file menu-items will be added here next
# menu_bar.add_cascade(label='file', menu=file_menu)
# menu_bar.add_cascade(label='edit', menu=file_menu)
# menu_bar.add_cascade(label='view', menu=file_menu)
# menu_bar.add_cascade(label='about', menu=file_menu)


def new_file():

    pass


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(
        defaultextension='.txt', filetypes=[('All Files', '*.*'),
                                            ('Text Documents',
                                             '*.txt')]
    )
    print(input_file_name)
    if input_file_name:
        '''We declared a file_name variable in the global scope to keep a track of the
    filename of the opened file. This is required to keep a track of whether a file
    has been opened. We need this variable in the global scope as we want this
    variable to be available to other methods such as save() and save_as().
    Not specifying it as global would mean that it is only available within the
    function. So, the save() and save_as() functions would not be able to
    check whether a file is already open in the editor'''

        global file_name
        file_name = input_file_name
        root.title('{} - {}      \n            {}'.format(os.path.basename(file_name),
                                    PROGRAM_NAME,
                               os.path.dirname(file_name)))
        content_text.delete(1.0, tk.END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())

def write_to_file(file_name):
    try:
        content = content_text.get(1.0, tk.END)
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(
        defaultextension='.txt', filetypes=[('All Files', '*.*'),
                                            ('Text Documents',
                                             '*.txt')]
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}      \n            {}'.format(os.path.basename(file_name),
                                                          PROGRAM_NAME,
                                                          os.path.dirname(file_name)))
    return 'break'



def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"


file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New',
                    accelerator='Ctrl+N',
                    compound='left',
                    underline=0,
                    image=new_file_icon,
                    command=new_file
                    )
file_menu.add_command(label='Open',
                    accelerator='Ctrl+O',
                    compound='left',
                    underline=0,
                    image=open_file_icon,
                    command=open_file
                    )
file_menu.add_command(label='Save',
                    accelerator='Ctrl+S',
                    compound='left',
                    underline=0,
                    image=save_file_icon,
                    command=save
                    )
file_menu.add_command(label='Save as',
                    accelerator='Ctrl+S',
                    compound='left',
                    underline=0,
                    command=save_as
                    )
file_menu.add_separator()
file_menu.add_command(label='Exit',
                    accelerator='Ctrl+Q',
                    compound='left',
                    underline=0,
                    command=new_file
                    )
menu_bar.add_cascade(label='File', menu=file_menu)

#functions for the edit menu tab
def cut():
    content_text.event_generate('<<Cut>>')
    return 'break'
def copy():
    content_text.event_generate('<<Copy>>')
    return 'break'
def paste():
    content_text.event_generate('<<Paste>>')
    return 'break'
def undo():
    content_text.event_generate('<<Undo>>')
    return 'break'
def redo(event=None):
    content_text.event_generate('<<Redo>>')
    return 'break'
def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return 'break'
def find_all(event=None):

    search_toplevel = tk.Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    tk.Label(search_toplevel,
             text='Find All:').grid(
        row=0, column=0, sticky=tk.E
    )
    search_entry_widget = tk.Entry(search_toplevel,
                                width=25)
    search_entry_widget.grid(row=0, column=1,
                             padx=2, pady=2,
                             sticky=tk.W+tk.E)
    search_entry_widget.focus_set()
    ignore_case_value = tk.IntVar()
    tk.Checkbutton(search_toplevel, text='Ignore Case',
    variable=ignore_case_value).grid(row=1, column=1,
                                     sticky=tk.E,
                                     padx=2, pady=2)
    tk.Button(search_toplevel, text='Find All', underline=0,
              command=lambda: search_output(
                  search_entry_widget.get()
                   ,ignore_case_value.get(), content_text,
              search_toplevel, search_entry_widget)).grid(row=0,
            column=2, sticky=tk.E + tk.W, padx=2, pady=2)
    def close_search_window():
        content_text.tag_remove('match', '1.0', tk.END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW',
                                 close_search_window)
    return 'break'

def search_output(needle, if_ignore_case, content_text,
                  search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', tk.END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
            nocase=if_ignore_case, stopindex=tk.END)
            print(start_pos)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            print(end_pos)
            content_text.tag_add('match', start_pos, end_pos)
            matches_found +=1
            start_pos=end_pos
        content_text.tag_config('match', foreground='red',
                                    background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))





edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo',
                      accelerator='Ctrl+Z',
                      compound='left',
                      underline=0,
                      image=undo_icon,
                      command=undo)
edit_menu.add_command(label='Redo',
                      accelerator='Ctrl+Y',
                      compound='left',
                      underline=0,
                      image=redo_icon,
                      command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut',
                      accelerator='Ctrl+X',
                      compound='left',
                      underline=0,
                      image=cut_icon,
                      command=cut)
edit_menu.add_command(label='Copy',
                      accelerator='Ctrl+C',
                      compound='left',
                      underline=0,
                      image=copy_icon,
                      command=copy)
edit_menu.add_command(label='Paste',
                      accelerator='Ctrl+V',
                      compound='left',
                      underline=0,
                      image=paste_icon,
                      command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find',
                      accelerator='Ctrl+F',
                      compound='left',
                      underline=0,
                      command=find_all)
edit_menu.add_separator()
edit_menu.add_command(label='Select All',
                      accelerator='Ctrl+A',
                      compound='left',
                      underline=7,
                      command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
show_line_number = tk.IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number',
                          variable=show_line_number)
show_cursor_info = tk.IntVar()
show_line_number.set(0)
view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom',
    variable= show_cursor_info)
highlight_line = tk.IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(
    label='Highlight Current Line',
    variable= highlight_line)
themes_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

color_schemes_unsorted = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}
color_schemes = sorted(color_schemes_unsorted)

theme_choice = tk.StringVar()
theme_choice.set('Default')
for k in color_schemes:
    themes_menu.add_radiobutton(label=k,
                                variable=theme_choice)
menu_bar.add_cascade(label='View', menu=view_menu)



about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About',
                      compound='left',
                      underline=0,
                      command=new_file)
about_menu.add_command(label='Help',
                      compound='left',
                      underline=0,
                      command=new_file)

menu_bar.add_cascade(label='About', menu=about_menu)
root.config(menu=menu_bar)

# add a Frame widget to hold the shortcut icons
shortcut_bar = tk.Frame(root, height=25,
                     background='light sea green')
shortcut_bar.pack(expand='no', fill='x')

# add a Frame widget to hold the line number bar
line_number_bar = tk.Text(root, width=23, padx=3,
                       takefocus=0,
                       border=0,background='khaki',
                       state='disable',
                       wrap='none')
line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

# add the main content Text widget and Scrollbar widget
content_text = tk.Text(root, wrap='word')
content_text.pack(expand=tk.YES, fill=tk.BOTH)
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
content_text.configure(font='{Helvetica 24 bold italic} 11' )
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

# handling redo quirk
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)

# handling select all
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)

# handling find all
content_text.bind('<Control-F>', find_all)
content_text.bind('<Control-f>', find_all)




if __name__ == '__main__':
    root.mainloop()



















from tkinter import *
from tkinter import filedialog

compiler = Tk()
compiler.title('GDAC IDE')

def run():
    code = editor.get('1.0', END)
    exec(code)

#code for Menu bar
menu_bar = Menu(compiler)

#Files menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=run)
file_menu.add_command(label='Save', command=run)
file_menu.add_command(label='Save As', command=save_as  )
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

#Menu bar
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

compiler.mainloop()
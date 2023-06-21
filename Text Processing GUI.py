from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
import tkinter.font as tkfont


def new_text():
    result = text.get(1.0, END)
    if len(result) != 1:
        answer = messagebox.askquestion('New text', 'Are you sure you want to continue?')
        if answer == 'yes':
            text.delete(1.0, END)


def open_dialog():
    file = filedialog.askopenfilename(title='Select a file to open')
    text.delete(1.0, END)
    f = open(file, 'r')
    text.insert(1.0, f.read())
    f.close()


def saving():
    file = filedialog.asksaveasfilename(title='Select a file to save', defaultextension='txt', filetypes=[('All Files', '*.*'), ('Text Files', '*.txt')])
    text_file = text.get('1.0', END)
    f = open(file, 'w')
    f.write(text_file)


def copying():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def cutting():
    copying()
    text.delete('sel.first', 'sel.last')


def pasting():
    text.insert(INSERT, text.clipboard_get())


def fontUp():
    global x
    global fontStyle
    x += 8
    fontStyle.configure(size=x)


def fontDown():
    global x
    global fontStyle
    x -= 8
    fontStyle.configure(size=x)


root = Tk()
root.title('Lab 5 Text Processing GUI')
root.geometry('600x450')
height = 600
width = 450

menubar = Menu(root)

fileMenu = Menu(menubar, tearoff=False)
fileMenu.add_command(label='New', command=new_text)
fileMenu.add_command(label='Open', command=open_dialog)
fileMenu.add_command(label='Save', command=saving)


editMenu = Menu(menubar, tearoff=False)
editMenu.add_command(label='Copy', command=copying)
editMenu.add_command(label='Cut', command=cutting)
editMenu.add_command(label='Paste', command=pasting)


menubar.add_cascade(label='File', menu=fileMenu)
menubar.add_cascade(label='Edit', menu=editMenu)


root.config(menu=menubar)


btn1 = Button(root, text='Increase Font Size', command=fontUp)
btn2 = Button(root, text='Decrease Font Size', command=fontDown)
btn1.pack(side=TOP)
btn2.pack(side=TOP)


x = int(14)
fontStyle = tkfont.Font(family='Arial', size=x)
text = Text(root, width=int(width*.80), height=int(height*.80), padx=1, pady=1, bd=2, wrap=WORD, font=fontStyle)
text.pack()


root.mainloop()

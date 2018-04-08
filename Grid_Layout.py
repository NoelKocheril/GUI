from tkinter import *

root = Tk()

name_label = Label(root,text="Name: ")
name_entry = Entry(root)

pass_label = Label(root,text="Pass: ")
pass_entry = Entry(root)

name_label.grid(row=0, sticky=E)
name_entry.grid(row=0,column=1)

pass_label.grid(row=1, sticky=E)
pass_entry.grid(row=1,column=1)

check = Checkbutton(root, text="Keep me Logged in?")
check.grid(row=2,columnspan=2)

root.mainloop()

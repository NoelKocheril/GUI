from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

Btn1 = Button(topFrame,text="Click Me",fg="red")
Btn2 = Button(topFrame,text="Click Me",fg="blue")
Btn3 = Button(bottomFrame,text="Click Me",fg="green")

Btn1.pack(side=LEFT)
Btn2.pack(side=RIGHT)
Btn3.pack()

theLabel = Label(leftFrame,text="This is a Label")
theLabel.pack(fill=Y)

root.mainloop()

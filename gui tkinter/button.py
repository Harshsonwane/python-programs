from tkinter import*
root=Tk()
root.geometry("650x450")
def name():
    print("teriahs kfkhjadsf")

def name1():
    print("dsffsdfteriahs kfkhjadsf")

def name2():
    print("ggfgteriahs kfkhjadsf")
    
frame=Frame(root,bg="gray",relief=SUNKEN)
frame.pack()
b1=Button(frame,fg="red",text="Print now" ,command=name)
b1.pack(side=LEFT,padx=3)

b2=Button(frame,fg="red",text="Print now" ,command=name1)
b2.pack(side=LEFT,padx=3)

b3=Button(frame,fg="red",text="Print now" ,command=name2)
b3.pack(side=LEFT,padx=3)

root.mainloop()

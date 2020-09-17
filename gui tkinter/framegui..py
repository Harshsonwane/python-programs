from tkinter import *
root=Tk()
root.geometry("650x550")
f1=Frame(root,bg="gray",border=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2=Frame(root,bg="red" ,border=6,relief=SUNKEN)
f2.pack(side=TOP ,fill="x")

f3=Frame(root,bg="black",border=3,relief=SUNKEN)
f3.pack(side=LEFT,fill="y")
f4=Frame(root,bg="red" ,border=6,relief=SUNKEN)
f4.pack(side=TOP ,fill="x")

l=Label(f1,text="thsis sd sd")
l.pack(pady=200)


l=Label(f2,text="thsis sd sd")
l.pack()

l=Label(f3,text="thsis sd sd")
l.pack()

l=Label(f4,text="thsis sd sd")
l.pack()
root.mainloop()

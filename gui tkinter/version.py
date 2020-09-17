from  tkinter import *
from PIL import Image,ImageTk
root=Tk()

root.geometry("360x360")
image=Image.open("sys.png")
photo=ImageTk.photoImage(image)
photo=PhotoImage(file="sys.png")
label=Label(imagephoto)
label1.pack()


root.mainloop()

from tkinter import *
root=Tk()

root.geometry("650x450")
def getval():
    print("its works")


    
Label(root,text="welodksd dsknddsffc").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="gender")
emergency=Label(root,text="emergency")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
   
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)

foodservice=checkbutton(text="want more or not",variable=foodservicevalue)
foodservice.grid(row=6,column=3)
Button(text="submit" ,command=getval).grid(row=7,column=3)
root.mainloop()

from tkinter import *
root=Tk()
def frame(root,side):
    w=Frame(root)
    e.pack(side=side,expand=YES,fill=both)
    return w
def button(root,side,text,command=None):
    w=Button(root,text=text,command=command)
    w.pack(side=side,expand=YES,fill=Both)
    return w
class Calculator(Frame):
    def _init_(self):
        Frame._init_(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("simple cali")
        self.master.iconname("calci1")

        display=StringVar()
        Entry(self,relief=SUNKEN,textvariable=display).pack(side=TOP,expand=YES,fill=BOTH)

        for key in ("123","456","789","-0."):
            keyF=frame(self,TOP)
            for char in key:
                button(keyF,LEFT,char,lambda w=display,s=' %s ' %char: w.set(w.get()+s))

        ops=frame(self,TOP)
        for char in "+-*/=":
            if char == '=' :
                btn=button(opf,LEFT,char)
                btn.bind('<ButtonRelease-1>',lambda e,s=self,w=display:s.calc(w),'+')
            else:
                btn=Button(opf,LEFT,char,lambda w=display,c=char:w.set(w.get()+' '+c+' '))


        clearF=frame(self,BOTTOM)
        button(clearF,LEFT,'Clr',lambda w=display:w.set(''))
        def clac(self,display):
            try:
                display.set('eval(display.get())')
            except ValueError:
                display.set("ERROR")
        if __name__=='__main__':
            calculator().mainloop()
        

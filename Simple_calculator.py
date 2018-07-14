
from tkinter import *
root=Tk()
root.title("Yuvi's CAl")
root.geometry('180x230')
global char
class cal:
    def __init__(self):
        self.string=StringVar()
        enter=Entry(root,textvariable=self.string)
        enter.grid(row=0,column=0,columnspan=6)

        values=["0","1","2","3","4","5","6","7","8","9","c",".","+","-","*","/","="]
        row=1
        col=2
        i=0
        for txt in values:
            if i==4:
                row=4
                col=2
            if i==8:
                row=8
                col=2
            if i==12:
                row=12
                col=2
            if i==16:
                row=16
                col=2
         
            if txt=="=":
                but=Button(root,text=txt,command=lambda:self.equals())
                but.grid(row=17,column=col,columnspan=12)
                but.config( height = 2, width = 15 ) 
            elif txt=="c":
                but=Button(root,text=txt,command=lambda:self.clr())
                but.grid(row=row,column=col)
                but.config( height = 2, width = 2 ) 
            else:
                but=Button(root,text=txt,command=lambda txt=txt:self.addc(txt))
                but.grid(row=row,column=col) 
                but.config( height = 2, width = 2 ) 
            
            col+=1
            i+=1
    def addc(self,char):
        
        self.string.set(self.string.get() + (str(char)))

        
    def equals(self):
            result=eval(self.string.get())
            self.string.set(result)
    def clr(self):
            self.string.set("")
           
cal()
mainloop()

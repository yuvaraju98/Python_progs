
from tkinter import *
root=Tk()
root.title("Yuvi's CAl")
global char
class cal:
    def __init__(self):
        self.string=StringVar()
        enter=Entry(root,textvariable=self.string)
        enter.grid(row=0,column=0,columnspan=6)
        
        values=["1","2","3","4","5","+","6","7","=","8","9","c"]
        row=1
        col=0
        i=0
        for txt in values:
            if i==3:
                row=3
                col=0
            if i==6:
                row=4
                col=0
            if i==9:
                row=5
                col=0
            
            if txt=="=":
                but=Button(root,text=txt,command=lambda:self.equals())
                but.grid(row=row,column=col) 
            elif txt=="c":
                but=Button(root,text=txt,command=lambda:self.clr())
                but.grid(row=row,column=col)
            else:
                but=Button(root,text=txt,command=lambda txt=txt:self.addc(txt))
                but.grid(row=row,column=col) 
            
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
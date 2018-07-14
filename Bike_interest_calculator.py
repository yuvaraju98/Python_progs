from tkinter import *
root=Tk()
class fi:
    def __init__(self):
        self.loan=StringVar()
        self.iny=StringVar()
        self.months=StringVar()
        lab5=Label(root,text="Loan Amount")
        lab5.pack()
        ent=Entry(root,textvariable=self.loan)
        ent.pack()
        lab6=Label(root,text="Interest")
        lab6.pack()
        ent1=Entry(root,textvariable=self.iny)
        ent1.pack()
        lab7=Label(root,text="Months:")
        lab7.pack()
        ent2=Entry(root,textvariable=self.months)
        ent2.pack()
        but=Button(root,text="submit",command=self.cal)
        but.pack()
        
    def cal(self):
        
        lo=float(self.loan.get())
        ine=float(self.iny.get())
        p=(lo*ine)/100
        ex=(p+lo)/int(self.months.get())
        print(ex)
        lab3=Label(root,text="Extra=")
        lab3.pack()
        
        lab=Label(root,text=p)
        lab.pack()
        lab4=Label(root,text="\n Per month=")
        lab4.pack()
        lab2=Label(root,text=ex)
        lab2.pack()
fi()       
mainloop()

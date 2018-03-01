print("hello")
import os
from tkinter import *
root = Tk()
root.geometry("500x500")
class auto:
    def cal(self):
        print(self.name.get())
        command="apt-cache search "+self.name.get()+" |column -s'-' >> pp.txt "
        os.system(command)
        fi=open("pp.txt", "r")
        f=fi.readlines()
        i=0
        a=[]
        for x in f:
            i+=1
            
            text=str(i)+" "+x;
            self.submitButton = Button(root, command=self.buttonClick, text="Submit")
            self.submitButton.pack()

    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        print('hello')  
           
        
    
    def inst(self,text):
        print("instal md"+text)
        
    def __init__(self):
        
        self.name=StringVar()
        lab5= Label(root,text="Software name")
        lab5.pack()
        ent=Entry(root,textvariable=self.name)
        ent.pack()
        but=Button(root,text="submit",command=self.cal)
        but.pack()
        
auto()
root.mainloop()










#print("hello")
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
        text=[]
        for x in f:
            i+=1
            Mylabel=Label(root,text=str(i)+" "+x).pack()
            text.insert(i,x)
            self.submitButton= Button(root,text="install"+str(i), command=lambda i=i:self.buttonClick(text[i-1])  )
            self.submitButton.pack()
            

    def buttonClick(self,text):
        print(text)
        fi=open("pp.txt","w")
        fi.write(text)
       

        
        os.system("sed -i -e 's/ -/*/g' pp.txt >> ppl.txt")
        
    
    
        
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










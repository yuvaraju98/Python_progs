#print("hello")
import os
from tkinter import *
import re
root = Tk()
root.geometry("500x600")

class auto:
    def cal(self):
        print(self.name.get())
        open("pp.txt","w")
        
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
       
        p=re.split(" - ",text)
        print("text")
        print(p[0])
        com2="apt-get install "+p[0]
        
        print(com2)
        c="apt update"
        root2=Tk()

        root2.geometry("200x200")
        Mylabel=Label(root2,text="Enter the System password ").pack()
        ent=Entry(root2,textvariable=c)
        ent.pack()
        but=Button(root2,text="submit",command=self.buttonClickexecute(com2,c))
        but.pack()
        
        os.popen("start terminal")
        #os.popen("sudo -S %s"%(c), 'w')
        #os.system(com2)
        
    def execute(self,com,c):
        #os.popen("sudo -S %s"%(c), 'w').write(c)
        print("Submitted")
        os.popen("sudo -S %s"%("apt update"), 'w').write(c)
        
    
        
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










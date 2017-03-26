import urllib, json

from urllib.request import *
from tkinter import *
global pincode
root=Tk()
root.title="Pincode"
frame=Frame(root,width=250,height=250)
frame.grid()
class cal:
    
    def __init__(self):
        na=Label(frame,text="Pincode:")
        na.grid(row=1,column=1)
        self.string=StringVar()
        entry=Entry(frame,textvariable=self.string)
        entry.grid(row=1,column=2,columnspan=6)
        but=Button(frame,text="submit",command=self.pin)
        but.grid(row=2,column=2)
    def pin(self):
        pincode=self.string.get()
        
        url = "https://www.whizapi.com/api/v2/util/ui/in/indian-city-by-postal-code?pin="+pincode+"&project-app-key=fnb1agfepp41y49jz6a39upx"
        
        res=urlopen(url).read().decode()
        lo=json.loads(res)
        f=open("name.txt","w")
        f.write(str(lo))
        City =lo['Data'][0]['City']
        add=lo['Data'][0]['Address']
        
        
        
        name=Label(frame,text="city:"+City)
        name2=Label(frame,text="address:"+add)
        
        name.grid(row=3,column=2)
        name2.grid(row=4,column=2)
        
        f.close()

        
        
        



cal()

mainloop()
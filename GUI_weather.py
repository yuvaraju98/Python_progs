import urllib, json
from urllib.request import urlopen
from tkinter import *

import os

root=Tk()
root.title("yuvi teck")
global pincode
class wea:
    def __init__(self):
        self.pin=StringVar()
        name=Label(root,text=" pin:")
        entry=Entry(root,textvariable=self.pin)
        name.grid(row=0,column=0)
        entry.grid(row=0,column=2,columnspan=6) 
        pincode=self.pin.get()
        but=Button(root,text="submit",command=self.ans)
        but.grid(row=2,column=3)
        
    def ans(self):
        key = "82ffaed9bf9c24c1"
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' +self.pin.get()+ '.json'
        res=urlopen(url).read().decode()
        lo=json.loads(res)
        f=open("name.txt","w")
        f.write(str(lo))
        try:
            weather =lo['current_observation']['weather']
            name1=Label(root,text=weather)
      
            name1.grid(row=3,column=0)
        except:
            name1=Label(root,text="Enter valid PNcode")
      
            name1.grid(row=3,column=0)

            
         
        
        
wea()      
root.mainloop()
        
        
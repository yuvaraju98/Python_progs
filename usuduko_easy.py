import numpy as np
arr = np.array([[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]])

def su(arr):
    list=[]
    list=[1,2,3,4,5,6,7,8,9]
    def col(i,list):
        for p in range(0,9):
            
            if arr[i][p] in list:
                
                list.remove(arr[i][p])
    def row(j,list):
        
        for o in range(0,9):
           
            if arr[o][j] in list:
                list.remove(arr[o][j])
    def block(i,j,list):
        
        if i<=2:
            a=2
            a1=0
        elif i>2 and i<=5:
            a=5
            a1=3
        else:
            a=8
            a1=6
            
        if j<=2:
            b=2
            b1=0
        elif j>2 and j<=5:
            b=5
            b1=3
        else:
            b=8
            b1=6
        
        for z in range(a1,a+1):
            for x in range(b1,b+1):
                
            
                if arr[z][x] in list:
                    list.remove(arr[z][x])
    qq=0               
    while 0 in arr:
        
        
        for i in range(0,9):
            for j in range(0,9):
                if arr[i][j]==0:
                    
                    col(i,list)
                    row(j,list)
                    block(i,j,list)
                    
                if len(list)==1:
                    
                    arr[i][j]=list[0]
                    list.remove(arr[i][j])
                else:    
                
                
                    list=[1,2,3,4,5,6,7,8,9]
        qq+=1          
    print(arr)
                    
su(arr)
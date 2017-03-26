import numpy as np
global f
'''
arr = np.array([[0,0,9,8,0,3,9,0,0],
                [0,0,0,2,0,0,6,0,0],
                [0,0,9,0,6,0,0,0,5],
                [3,0,0,0,0,6,0,0,0],
                [0,0,2,0,9,0,5,0,0],
                [0,0,0,3,0,0,0,0,6],
                [9,0,0,0,4,0,8,0,0],
                [0,0,4,0,0,5,0,0,0],
                [2,0,8,6,0,1,0,0,7]])
'''


f = open('words.txt')
for word in f.read().split():
    print(word)


cc=arr
def su(arr,f):
    list=[]
    list=[1,2,3,4,5,6,7,8,9]
    def sudu(arr,list,f):
        global r,h,k
        
        for i in range(0,9):
            for j in range(0,9):
                if arr[i][j]==0:
                    
                    col(i,list)
                    row(j,list)
                    block(i,j,list)
                    
                if len(list)==1:
                    print(list)
                    arr[i][j]=list[0]
                    list.remove(arr[i][j])
                
                elif len(list) is 2 and f is not 1:
                    print("lenfht is 2")
                    arr[i][j]=list[0]
                    col(i,list)
                    row(j,list)
                    block(i,j,list)
                    h=i
                    k=j
                    
                    r=[]
                    r=list
                    f=1
                    yes(f)
                else:
                    list=[1,2,3,4,5,6,7,8,9]
                '''elif f==1:
                    print("first didnt work")
                    arr[h][k]=r[1]
                    f+=1
                    yes(f)
                   ''' 
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
        
        for z in range(a1,a):
            for x in range(b1,b):
                if arr[z][x] in list:
                    list.remove(arr[z][x])
    for i in range(0,9):
            for j in range(0,9):
                if arr[i][j]==0:
                    sudu(arr,list,f)
def yes(f):
    
    for i in range(0,9):
        for j in range(0,9):
                if arr[i][j]==0:
                    su(arr,f)
f=0
yes(f)

print(arr)


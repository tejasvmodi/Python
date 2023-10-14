def list(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

d=[10,20,30,40,50]
e=[10,20,30,40,50]

if(len(d)==len(e)):
    d1=list(d,e)
    print(d1)





        

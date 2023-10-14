def func(num1,num2):
    list1=[]
    list2=[]
    list3=[]
    c=0
    d=0
    for i in range(1,num1+1):
        if(num1%i==0):
            list1.insert(c,i)
            c=c+1
    for j in range(1,num2+1):
        if(num2%j==0):
            list2.insert(d,j)
            d=d+1
    for k in range(1,len(list1)):
        c1=0
        for m in range(1,len(list2)):
            if(list1[k]==list2[m]):
                    list3.insert(c1,list1[k])
                    c1=c1+1
    if(len(list3)==0):
        return 1
    else:
        return max(list3)

i1=int(input("enter the number1 :"))
j1=int(input("enter the number2 :"))
c1=func(i1,j1)
print("The GCD of two numbers are ",c1)
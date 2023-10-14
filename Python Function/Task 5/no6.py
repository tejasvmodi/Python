def feinch(val1,val2,val3,val4):
    inch=val3+val4
    feet=val1+val2

    while(inch >11 ):
        feet=feet+1
        inch=inch-12
    
    return feet,inch

f1=int(input("Enter the 1st value of feet  : "))
f2=int(input("Enter the 2nd value of feet  : "))
i1=int(input("enter the 1st value of inch : "))
i2=int(input("Enter the 2nd value of inch :"))

v=feinch(f1,f2,i1,i2)
print("the feet is ",v[0],"and the inch is ",v[1])




def arm(val):
    v3=0
    v4=str(val)
    for i in range(0,len(v4)):

        v1=val%10
        v2=v1*v1*v1
        v3=v3+v2
        val=val//10
   # print(v3 ,"and",v4)
    if(v3==int(v4)):
    
        print("the number",v3," is armstrong")
    else:
        print("the number is not a armstrong ")


i=int(input("enter the number "))
print(arm(i))

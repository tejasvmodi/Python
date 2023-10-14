# perfect number
var1=int(input("enter the number"))
sum=0
for i in range(1,var1):
    if(var1%i==0):
        sum=sum+i

if(var1==sum):
    print("thhe number is perfect")
else:
    print("not a perfect number")
var=int(input("enter the number"))
t=str(var)
sum=0
while(var>0):
    r=var%10
    sum=(sum*10)+r
    var=var//10

if(t==str(sum)):
  
    print("number is pellindrom")
else:
    print("nummber is not pellindrom")


i=int(input("enter the number "))
temp=str(i)
sum=0

while(i>0):
    r=i%10
    sum=(sum*10)+r
    i=i//10


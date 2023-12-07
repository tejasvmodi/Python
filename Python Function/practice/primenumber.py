c=int(input("enter the number "))
P=0
for i in range(2,c):
    if(c%i==0):
        print("it is not prime number")
        P=P+1
    else:
        print("it is  prime number")
        
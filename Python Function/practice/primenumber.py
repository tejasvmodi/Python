c=int(input("enter the number "))
for i in range(2,c):
    if(c%i==0):
        print("it is not prime number")
        c=c+1
    else:
        print("it is  prime number")
        
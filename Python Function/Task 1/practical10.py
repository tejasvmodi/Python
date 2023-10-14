# prime number
var=int(input("enter the numer"))

for i in range(2,var):
    if(var%i==0):
        print("number is not prime")
        break
    else:
        print("number is prime ")
        break
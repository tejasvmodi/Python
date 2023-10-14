def fact(number):
    c=1
    for i in range(1,number+1):
        c=c*i
    return c

i=int(input("enter the  number "))
c=fact(i)
print("Factorial number is  ",c)
        
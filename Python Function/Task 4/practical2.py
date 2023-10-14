# Write a python function to print all the prime numbers between the specific
# range given bt user
def prime(start,end):
    for i in range(start,end+1):
        flag=0
        for j in range(2,i):
            if(i%j==0):
                flag=1
        if(flag==0):
            print("Prime number is :",i)
ic=int(input("enter the starting point :"))
id=int(input("enter the ending point :"))
print(prime(ic,id))
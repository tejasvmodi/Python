var = int(input("Enter the number "))
c=0
d=0
for i in range(1,var):
    if(i%2==0):
        d=d+1
    else:
        c=c+1
print("the odd number in list is ",c)
print("the even number in list is ",d)
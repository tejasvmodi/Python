def func(val):
    global sum
    if(val==0):
        return 0
    else:
        sum=val+func(val-1)
        return sum
i=int(input("Enter the number "))
d=func(i)
print("sum of predecessor is ",d)

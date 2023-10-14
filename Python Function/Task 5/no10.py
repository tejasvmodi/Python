def fibo(val):
    global c
    if val<=1:
        return val
    else:
        c=fibo(val-1)+fibo(val-2)
        return c
i = int(input("Enter the number "))
for i in range(i+1):
    print(fibo(i),end=" ")
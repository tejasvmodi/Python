def i(limit):
    c=1
    for i in range(1,limit+1):
        for j in range(1,i):
            print(c,end=" ")
            c=c+1
        print()

    
i1=int(input("enter the number "))
print(i(i1))
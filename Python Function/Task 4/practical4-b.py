def p(limit):
    for i in range(1,limit+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    
    for k in range(1,limit+1):
        for p in range(k,limit):
            print("*",end=' ')
        print()


i=int(input("enter the number "))
print(p(i))

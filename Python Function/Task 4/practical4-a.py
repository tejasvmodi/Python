def d(lim):
    for i in range(1,6):
        if(i%2==0):
            for j in range(1,lim+1):
                if(j%2==0):
                    print("1",end=" ")
                else:
                    print("0",end=" ")
            print()
        else:
                for k in range(1,lim+1):
                    if(k%2==0):
                       print("0",end=" ")
                    else:
                        print("1",end=" ")
                print()
            
            
i=int(input("enter the number :"))
print(d(i))


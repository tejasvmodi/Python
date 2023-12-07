i=int(input('enter the ending point :'))
sum=0
num=1
try:
    if i<=0:
        raise Exception("the value is not less than one ")
    else:
        while(num!=i):
            sum=sum+(num*num)
            num=num+2
        
        print("the solution of the series is ",sum)
finally:
    print("complete execution...")

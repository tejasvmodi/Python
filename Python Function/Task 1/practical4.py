# print the largest number
var1=int(input("enter the number1"))
var2=int(input("enter the number2"))
var3=int(input("enter the number3"))

if(var1>var2):
    if(var1>var3):
        print("the largest number is ",var1)
elif(var3<var2):
    print("the largest number is ",var2)
else:
    print("the largest number is ",var3)

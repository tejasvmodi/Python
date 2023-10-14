# print the percentage 
var1=int(input("enter the percentage"))

if(var1 >=85):
    print("your grade is A")
elif(var1 <85 and var1 >=75):
    print("your grade is B")
elif(var1 < 75 and var1>=65):
    print("your grade is C")
elif(var1 < 65 and var1>=55):
    print("your grade is D")
elif(var1 < 55 and var1>=40):
    print("the grade is E")
else:
    print("the grade is F")
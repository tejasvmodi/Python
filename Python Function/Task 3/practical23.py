import random
var=int(input("Enter the number bettween 1 to 10 "))
r=random.randrange(1,11)
while(var!=r):
    var=int(input("not match enter another number "))
if(var==r):
    print("guess is right ")
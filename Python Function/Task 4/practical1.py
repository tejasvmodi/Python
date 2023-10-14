# Write a python function for calculating cube of the number.
# Define a second function called by_three that takes an argument called
# number. if that number is divisible by 3, by_three should call cube(number)
# and return its result. Otherwise, by_three should return False.
def cube(number):
    return number*number*number

def by_three(num):
    if(num%3==0):
        res=cube(num)
        return res
    else:
        return False

i=int(input("Enter the number which is divisable by three :"))
s=by_three(i)
print(" the ans is : ",s)
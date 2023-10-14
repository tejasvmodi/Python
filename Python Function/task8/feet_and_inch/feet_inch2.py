import feet_inch as fet1

def main():
    f1=int(input("enter the feet: "))
    i1=int(input("enter the inch: "))
    f2=int(input("enter the feet2: "))
    i2=int(input("enter the inch2: "))

    obj1=fet1.fet(f1,i1)
    obj2=fet1.fet(f2,i2)
    feet1,inch1=obj1.feet_inch(obj2)
    print("the total feet is ",feet1,"and the total inch is ",inch1)

main()
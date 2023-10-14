import calculator.scientificcal as cal
import calculator.simplecal as calculator

# def val():
#     val=int(input("enter the value1 "))
#     sec=int(input("enter the value2 "))
#     return val,sec

def main():
    while True:
        print("1. for sum")
        print("2. for sub")
        print("3. for mul")
        print("4. for div")
        print("5. for sin")
        print("6. for cos")
        print("7. for tan")
        print("8. for power ")
        print("9. for exit")

        print()
        choice=int(input("enter the number "))
        print()
        match choice:
            case 1:
                 val=int(input("enter the value1 "))
                 sec=int(input("enter the value2 "))
                 c=calculator.sum(val,sec)
                 print("the sum is ",c)
            case 2:
                val3=int(input("enter the value1 "))
                val4=int(input("enter the value2 "))
                d=calculator.sub1(val3,val4)
                print("the sub is ",d)
            case 3:
                val3=int(input("enter the value1 "))
                val4=int(input("enter the value2 "))
                d=calculator.mul(val3,val4)
                print("the mul is ",d)
            case 4:
                val3=int(input("enter the value1 "))
                val4=int(input("enter the value2 "))
                d=calculator.div(val3,val4)
                print("the division is ",d)
            case 5:
                val3=int(input("enter the angle : "))
                d=cal.sin1(val3)
                print("the sub is ",d)
            case 6:
                val3=int(input("enter the angle : "))
                d=cal.cos1(val3)
                print("the sub is ",d)
            case 7:
                val3=int(input("enter the angle : "))
                d=cal.tan1(val3)
                print("the sub is ",d)
            case 8:
                val3=int(input("enter the value1 "))
                val4=int(input("enter the value2 "))
                d=cal.po(val3,val4)
                print("the division is ",d)
            case 9:
                 break
            
main()
                



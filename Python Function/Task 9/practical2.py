f=int(input("enter the number 1: "))
s=int(input("enter the second number 2: "))
while True:
    print("1. for summation")
    print("2. for substraction ")
    print("3. for multiplication ")
    print("4. fro division")
    choice=int(input("enter the choice "))
    match choice:
        case 1:
            print(f+s)
        case 2:
            print(f-s)
        case 3:
            print(f*s)
        case 4:
                try:
                    c=f/s
                    print(c)
                except :
                    print("the number is not divided by zero ")
                    exit()
        
        case defalut:
              print('existing the program ')
        

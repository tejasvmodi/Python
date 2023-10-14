import euclidiean_1 as euc

def main():
    x1=int(input("enter the x1: "))
    y1=int(input("enter the y1: "))
    x2=int(input("enter the x2: "))
    y2=int(input("enter the y2: "))

    c=euc.eucli(x1,y1,x2,y2)
    print("the eucldiean distance is ",c)

main()


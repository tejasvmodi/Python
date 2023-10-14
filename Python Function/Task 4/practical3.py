def sum(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

def cal(operation,n1,n2):
    match operation:
        case 0:
            s=sum(n1,n2)
            return s
        case 1:
            s=sub(n1,n2)
            return s
        case 2:
            d=mul(n1,n2)
            return d
        case 3:
            m=div(n1,n2)
            return m
        case default:
            s="wrong number added"
            return s
    

n1=int(input("enter the number 1 :"))
n2=int(input("Enter the number 2 :"))
n3=int(input("Enter the operation number 0 for sum,1 for sub, 2 for mul, 3 for division: "))
ans=cal(n3,n1,n2)
print("the ans is ",ans)


# def pelindrom(val1):
def pel(var1):
    rev=0
    temp=var1
    while temp > 0 :
        i=temp % 10
        rev= (rev *10) + i
        temp=temp//10

    if(var1==rev):
        print("The number is pelindrome")
    else:
        print("The number is Not Pelindrome")


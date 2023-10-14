def li(a):
    total=0
    avg=0
    for i in a:
        total+=i
        avg=total/len(a)
    return total,avg

i=int(input("enter the total numbers "))
d=[]
for j in range(1,i+1):
    c1=int(input("Enter the number "))
    d.insert(j-1,c1)
c=li(d)
print("sum of the elements are ",c[0])
print("avg of the element are ",c[1])
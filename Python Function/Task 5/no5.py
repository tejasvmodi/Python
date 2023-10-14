def salary(b_salary=9000):
    DA=0.10
    HRA=0.15
    v= b_salary*DA*HRA
    return v
n=input('enter the name ')
d=input('enter the department ')
i= input("enter the salary ")
if(i==''):
    net=salary()
else:
    net=salary(int(i))
print("employee name is ",n)
print("employee department is ",d)
print("employee salary is ",net)
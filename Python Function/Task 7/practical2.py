emp=[]
class employee():
    def __init__(self,id,name,salary,designation,experiance):
        self.id=id
        self.name=name
        self.salary=salary
        self.designation=designation
        self.experiance=experiance
    
    def add(self):
        emp.append(self)
        print()
        print("employee detail added successfully ")
    
    def display(self,obj):
                print()
                print("the employee id is ",{obj.id})
                print("the employee name is ",{obj.name})
                print("the employee salary is ",{obj.salary})
                print("the desognation of the employee is ",{obj.designation})
                print("the experience of employee is ",{obj.experiance})
    
    def update(self,obj,sname):
        for i in emp:
            if i.id==obj:
                i.name=sname
        print()
        print("the employee name is updated ")       

    def delete(self,obj):
         emp.remove(obj)
         return "the employee is removed"
           

def main():
    obj=employee(1,"Tejasv",25000,"Manager",8)
    while True:
        print()
        print("1. enter the employee details")
        print("2. search the employee from the ID")
        print("3. update the employee name by using ID ")
        print("4. remove the employee")
        print("5. display all employee details ")
        print("6. exit")

        a=int(input("enter the number  "))
        match a:
            case 1:
                print()
                a1=int(input("enter the employee id "))
                b=input("enter the employee name ")
                c=int(input("enter the employee salary "))
                d=input("enter the desognation of the employee ")
                e=int(input("enter the experience of employee "))

                obj1=employee(a1,b,c,d,e)
                obj1.add()
            
            case 2:
                  print()
                  idel=int(input("enter the id "))
                  for i in emp:
                       if i.id==idel:
                            obj.display(i)
            
            case 3:
                  print()
                  abdc=int(input("enter the number: "))
                  abc=input("enter the name: ")
                  obj.update(abdc,abc)
                
            case 4:
                  print()
                  a=int(input("enter the id"))
                  for i in emp:
                    if i.id==a:
                        obj.delete(i)
            case 5:
                  print()
                  for i in emp:
                    print()
                    print("the employee id is ",{i.id})
                    print("the employee name is ",{i.name})
                    print("the employee salary is ",{i.salary})
                    print("the desognation of the employee is ",{i.designation})
                    print("the experience of employee is ",{i.experiance})
                      
                
            case 6:
                  break

main()
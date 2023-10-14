class salary(object):
    def __init__(self,name,department,basic_salary):
        self.name=name
        self.department=department
        self.basic_salary=basic_salary

    def total_salary(self):
       
        self.da=self.basic_salary *0.1
        self.hra=self.basic_salary * 0.15
        total_salary = self.basic_salary + self.da +self.hra
        return total_salary

def main():
    obj1=salary(name='tejasv modi',department='MscIt',basic_salary=10000)
    obj2=obj1.total_salary()
    print(obj2)

main()
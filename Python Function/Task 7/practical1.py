#student management system
l1=[]
class Student():
    
    def __init__(self, rollnumber,name,mark1,mark2 ):
        self.rollnumber=rollnumber
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
    
    def add(self):
        l1.append(self)
        print()
        print("the record is added successfully")

    def disply(self,obj):
        print()
        print("the rollnumber is",{obj.rollnumber})
        print("the name is ",{obj.name})
        print("marks of the subject 1 is",{obj.mark1})
        print("marks of the subject 2 is",{obj.mark2})
    
    
    def delete(self,obj):
        l1.remove(obj)
        return "the student remove successfully"
         
    def update(self,obj,abd):
        for i in l1:
            if i.rollnumber== obj:
                i.rollnumber=abd
                print()
                print("the number is update")
            else:
                print("the roll number is not in list")
            





def main():
    std=Student(11,'tejasv',70,90)
    while True:
        print()
        print("1.enter the student details ")
        print("2.search the student  ")
        print("3.show all details of the student ")
        print("4.update student detail ")
        print("5.delete the student ")
        print("6. for exit ")
        choice =int(input("enter the number between 1 to 5  "))
        match choice:
            case 1:
                # print("enter the student rollnumber,name,mark1,mark2")
                rollnumber=int(input("enter the rollnumber"))
                name=input("enter the name ")
                mark1=input("enter the subject 1 marks")
                mark2=input("enter the subject 2 marks")
                print()
                print()
                std=Student(rollnumber,name,mark1,mark2)
                std.add()
            case 2:
                print()
                search=int(input("enter the roll number of the student which you want to search"))
                for i in l1:                   
                    if  i.rollnumber==search:
                        print()
                        print("the student name is",i.name)
                        print("the student name is",i.rollnumber)
                        print("the student name is",i.mark1)
                        print("the student name is",i.mark2)
                    
            case 3:
                for i in l1:
                    std.disply(i)
            case 4:
                 print()
                 a=int(input("enter the roll number you want to update"))
                 c=int(input("enter the new roll number"))
                 std.update(a,c)
                     
            case 5:
                print()
                a=int(input("enter the roll number"))
                for i in l1:
                     if i.rollnumber==a:
                        std.delete(i)
            case 6:
                   break
            
                


                
main()

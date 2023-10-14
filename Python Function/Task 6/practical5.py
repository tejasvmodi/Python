class mark(object):
    def __init__(self,name,sem,marks):
        self.name=name
        self.sem=sem
        self.marks=marks
    
    def mar(self):
        sum=0
        for i in self.marks:
            sum = sum+i
        return sum/len(self.marks)
def main():
    obj1=mark(name='tejasv modi',sem=5,marks=[80,40,50,60,80,99])
    print(obj1.mar())

main()
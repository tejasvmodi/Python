class height(object):
    def __init__(self,inch1,inch2,feet1,feet2):
        self.inch1=inch1
        self.feet1=feet1
        self.inch2=inch2
        self.feet2=feet2

    def h(self):
        t_inch=self.inch1+self.inch2
        t_feet=self.feet1+self.feet2
        if t_inch < 12:
            t_inch=t_inch //12
            t_feet = t_feet+1
        return t_inch,t_feet
    
def main():
    feet1=int(input("Enter Feet 1: "))
    feet2=int(input("Enter  Feet 2: "))
    inch1=int(input("Enter  Inch 1: "))
    inch2=int(input("Enter  Inch 2: "))

    if inch1>11 or inch2>11:
        print("enter the inch under the 11 ")
    else:
        obj=height(feet1=feet1,feet2=feet2,inch1=inch1,inch2=inch2)
        print(obj.h())        
    
main()

    
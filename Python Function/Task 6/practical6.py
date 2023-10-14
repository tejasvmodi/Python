class complex(object):
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def com(self,x,y):
        self.x = x.r + y.r
        self.y = x.i + y.i
        return complex(self.x,self.y)
    
    def mul(self,x1,y1):
        self.x = x1.r * y1.r
        self.y = x1.i * y1.i
        return complex(self.x,self.y)
    
def main():
    obj1=complex(10,20)
    obj2=complex(30,50)
    obj3=complex()
    obj4=complex()
    obj3=obj3.com(obj1,obj2)
    obj4=obj4.mul(obj1,obj2)

    print("thesum imaginary number",obj3.i)
    print("the sum real  number ",obj3.r)
    print("the mul imaginary number",obj4.i)
    print("the mul real  number ",obj4.r)

main()
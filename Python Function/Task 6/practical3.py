import math
class point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def ec(self,p):
        return math.sqrt(((self.x-p.x)**2) +( (self.y-p.y)**2) )

def main():
    obj1=point(5,2)
    obj2=point(3,2)

    print(obj2.ec(obj1))

main()
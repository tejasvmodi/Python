class len(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        return self.length * self.width

def main():
    obj2=len(30,10)
    print("the area is ",obj2.area())

main()
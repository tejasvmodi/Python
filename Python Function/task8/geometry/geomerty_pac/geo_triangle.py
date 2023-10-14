class tri:
    def __init__(self,base,height,side1):
        self.base=base
        self.height=height
        self.side1=side1

    def area(self):
        return 0.5 * self.base * self.height
    
    def primeter(self):
        return self.base * self.height * self.side1

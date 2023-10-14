class Fact(object):
    def __init__(self,numerator=1,denominator=1):
        self.denominator=denominator
        self.numerator=numerator

    def add(self,f):
        if self.denominator==f.denominator :
            return (self.numerator + f.numerator),self.denominator
        else:
            n1=(self.numerator * f.denominator)+(self.denominator * f.numerator)
            n2=self.denominator * f.denominator
            return n1,n2
    
    def mul(self,m):
        if self.denominator==m.denominator:
            return (self.numerator * m.numerator),self.denominator
        else:
            n1=(self.numerator * m.denominator)*(self.denominator * m.numerator)
            n2=self.denominator * m.denominator
            return n1,n2
    
def main():
    obj1=Fact(1,4)
    obj2=Fact(1,4)

    n,d=obj2.add(obj1)
    print(n ,"/", d)

    m,l=obj2.mul(obj1)
    print(m,"/",l)

main()

# class Fraction(object):
#     def __init__(self, numerator=1,denominator=1):
#         self.numerator=numerator
#         self.denominator=denominator

#     def add(self,fraction):
#         if self.denominator==fraction.denominator:
#             return (self.numerator+fraction.numerator),self.denominator
#         else:
#             n1=(self.numerator*fraction.denominator)+(self.denominator*fraction.numerator)
#             n2=self.denominator*fraction.denominator
#             return n1,n2

         
#     def multiply(self,fraction):
#         if self.denominator==fraction.denominator:
#             return (self.numerator*fraction.numerator),self.denominator
#         else:
#             n1=(self.numerator*fraction.denominator)*(self.denominator*fraction.numerator)
#             n2=self.denominator*fraction.denominator
#             return n1,n2

# def main():
#     obj1=Fraction(1,2)
#     obj2=Fraction(3,8)

#     num,deno=obj2.add(obj1)
#     print(f"Addition =>{num}/{deno}")

#     num,deno=obj2.multiply(obj1)
#     print(f"multiplication =>{num}/{deno}")    

# main()


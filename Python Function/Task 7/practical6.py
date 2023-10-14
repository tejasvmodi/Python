class Vehical():
    def __init__(self,no,type,price):
        self.no=no
        self.type=type
        self.price=price

    def display(self):
        print("the model no is ",self.no)
        print("the type pf vehicle is ",self.type)
        print("the price of vehicle is ",self.price)
    
class car(Vehical):
    def __init__(self, no, type, price,engine_number,color,fueltype):
        Vehical.__init__(self,no, type, price)
        self.engine_number=engine_number
        self.color=color
        self.fueltype=fueltype

    def display(self):
       print("the color of the car is ",{self.color})
       print("the engine number is ",{self.engine_number})
       print("the fueltype of the class is ",self.fueltype)
       Vehical.display(self)
       print()

class Bike(Vehical):
    def __init__(self, no, type, price,cc,mileage):
        Vehical.__init__(self,no, type, price)
        self.cc=cc
        self.mileage=mileage
    
    def display(self):
        print("the cc of the bike is ",{self.cc})
        print("the mileage of the bike ",{self.mileage})
        Vehical.display(self)
        print()

def main():
    Bike1=Bike("Hero Honda","CT 100",50000,63.5,50)
    car1=car(1,"Sedan",56200,6987451236,'Black','Petrol')

    Bike1.display()
    car1.display()

main()
from multipledispatch import dispatch
import math

class Area:

    @dispatch(int)
    def area(self,len):
       print("Area of cube is: ",6*len**2)

    @dispatch(float)
    def area(self,rad):
        print("Area of Shpare is: ",4*math.pi*rad**2)

    @dispatch(float,int)
    def area(self,rad,height):
        print("Area of cylinder is: ",2*math.pi*rad*(rad+height))

obj=Area()
obj.area(5)
obj.area(4.0)
obj.area(1.0,3)

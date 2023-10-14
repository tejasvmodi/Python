from geomerty_pac import geo_circle,geo_rectangle,geo_triangle

def main():
    d=geo_circle.cir(radius=12)
    e=geo_rectangle.rect(length=12,width=13)
    f=geo_triangle.tri(base=12,height=23,side1=22)


    print("the raduis of circle is ",d.area())
    print("the premeter of the circle is ",d.premeter())

    print("the raduis of rectangle is ",e.area())
    print("the premeter of the rectangle is ",e.primeter())
    
    print("the raduis of circle is ",f.area())
    print("the premeter of the circle is ",f.primeter())

main()
    
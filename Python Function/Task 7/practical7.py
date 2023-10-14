number=[10,20,0,-10,-20,-30,30]

positive=list(filter(lambda p:p>0,number))
negative=list(filter(lambda n:n<0,number))
zero =list(filter(lambda z:z==0 ,number))

print("the positive number is ",positive)
print("the negative list is ",negative)
print("the zero list is ",zero)
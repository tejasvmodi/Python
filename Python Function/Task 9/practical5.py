s=int(input("enter the size of array "))
num=[]
try:
    if(s<=0):
        raise Exception("size not be negative or zero")
    elif(s>10):
        raise Exception("the size of the array not greate than 10")
        
    else:
        for i in range(s):
            num.append(int(input("enter  number")))
        
        print("the max number from the array is ",max(num))
        print("the min number from the array is ",min(num))            

except Exception as r:
    print("complete execution because ",r)
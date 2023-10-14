c=[1,4,5,14,21,20,35,40]
mul=list(filter(lambda x:x%7==0,c))
print("the multiple of 7 is ",mul)

num=list(map(lambda i:i+10,c))
print(" the sum is ",num)

# s=list(filter(lambda i:i+10,c))
# print(" the sum is ",num)
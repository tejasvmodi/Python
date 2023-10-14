second = int(input("Enter the seconds "))
hours = 0
minutes = second //60
second = second % 60
while(minutes > 59):
    hours=hours+1
    minutes= minutes-60
while(second > 59):
    minutes = minutes +1
    second=second -60
print(hours," : ",minutes," : ",second )
#print(minutes)

#print(hours)
#print(second)


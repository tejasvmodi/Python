# t1=[]
# while True:
# 	i=int(input("enter 1 for push  , 2 to pop and 3 to display"))
# 	if(i==1):
# 		j=int(input("enter the count of numbers"))
# 		for j1 in range(0,j):
# 			k=int("enter the value")
# 			t1.append(k)
# 		print(t1)
# 	elif(i==2):
# 		t1.pop()
# 		print(t1)
# 	elif(i==3):
		
# 			print(t1)
	



top=-1
t1=[]
def push(value):
	global top
	top+=1
	t1.append(value)

def pop():
	if(top==-1):
		return "Stack is empty"
	else:
		print(t1.pop(),"is deleted")
		
	
def dis():
	if(top==-1):
		return "Stack is empty"
	else:
		for i in range(0,top):
			print(t1[i],end=" ")



while True:

	print("Enter 1 for push")
	print("enter 2 for pop")
	print("enter 3 for display")
	print("enter 4 for exit")
	i=int(input("Enter the number"))
	if(i==1):
		i1=input("enter value")
		push(i1)
	elif(i==2):
		print(pop())
	elif(i==3):
		print()
		print(dis())
	else:
		break



rear=-1
front=-1
q1=[]
def insert(value):
    global rear,front
    rear=rear+1
    q1.append(value)
    if (front==-1):
        front=0
    


def delete():
	global rear,front
	if front==-1:
		print("Queue is Empty")
		return
	else:
		val=q1[front]
		if (rear==front):
			rear=-1
			front=-1
		else:
			front=front+1
		return val

def display():
    global rear ,front
    if(front==rear):
        print("queue is empty")
    else:
        for i in range(front,rear+1):
            print(q1[i], end=" ")
    


while True:
    print("Enter 1 for insertion")
    print("enter 2 for deletion")
    print("enter 3 for display")
    print("enter 4 for exit")

    i =int(input("enter the number "))
    match i:
        case 1:
            i1=input("enter the value")
            insert(i1)
        case 2:
            print()
            print(delete(),"is deleted")
        case 3:
            print()
            print(display())
        case default:
            break



    


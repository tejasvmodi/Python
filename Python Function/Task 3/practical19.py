var=input("enter the amount : ")

s=var.split(".")

if(len(s) >1):
    print("amount is ",s[0]," ruppes and ",s[1]," paisa")
else:
    print("amount is ",s[0]," ruppes and 00 paisa")

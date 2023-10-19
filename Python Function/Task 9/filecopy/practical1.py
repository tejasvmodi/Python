
filename=input("enter the file name: ")
textfile1=input("enter the content of the file :")
print("file name of backup file must be 'smit'")
choose=input("Enter the second filename for backup : ")
try:

    
    if(choose=='smit'):
        r=open(filename,"w")
        r.write(textfile1)
        s=open(choose,"w")

    r=open(filename,"r")

    # while f1.read != None :
    s.write(r.read())

except:
    print("the second file is not exist")




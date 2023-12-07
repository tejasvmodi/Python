# Write a Python code, for copying the content of one file to another file.

file1=input("enter the file name ")
data=input("enter the data of the file ")

a=open(file1,"w")
a.write(data)

print(file1," is created....")
file123=input("enter the name of file you want to copy the data...")

b=open(file123,"w")
a=open(file1,"r")
b.write(a.read())



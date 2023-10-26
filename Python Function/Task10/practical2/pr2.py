# Write a Python code to count the number of words and lines in the input file and display the result.

f=open("abc")
c=0
for i in f.read():
    if(i==' '):
        c=c+1
    
    elif i=='\n':
        c=c+1
print("the words in the file is ",c+1)
b=0
c1=open("abc","r")
for e in c1:
    b=b+1

print("the lines in the file is",b)

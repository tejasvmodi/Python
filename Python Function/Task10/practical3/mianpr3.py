# Write a Python program that encrypts the contents of a text file using a simple encryption algorithm. Decrypt the file and display on console.

def enfun():
    f=open("smit","r")
    r=open("tejasc","w")
    for i in f:
        for j in i:    
            r.write(chr(ord(j)+4))


def defun():
    r=open("tejasc","r")
    for i in r:
        for j in i:
            print(chr(ord(j)-4),end="")

enfun()
defun()
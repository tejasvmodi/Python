class Noteligible(RuntimeError):
    def __init__(self,error):
        self.error=error
        
    
name=input("enter the name")
age=int(input("enter the age for voting"))
gender=input("enter the gender")

try:
    if age< 18:
        raise Noteligible("you are underage for the voting ")
    else:
        print("Name of Voting card ",name)
        print("Age of the voter ",age)
        print("gender of the voter ",gender)
except Noteligible as n:
    print(n)
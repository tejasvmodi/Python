
class person():
    def __init__(self,name,code):
        self.name=name
        self.code=code

class Account(person):
    def __init__(self, name, code,pay):
        person.__init__(self,name, code)
        self.pay=pay
    
class Admin(person):
    def __init__(self, name, code,experience):
        person.__init__(self,name, code)
        # self.admin_name=admin_name
        self.experience=experience

class AccountMaster(Account,Admin):
    def __init__(self, name, code, pay,experience):
        Account.__init__(self,name, code, pay)
        Admin.__init__(self,name,code,experience)
  
    def abc(self):
        print("enter the name ",{self.name})
        print("enter the code ",{self.code})
        print("enter the pay ",{self.pay})
        print("enter the experience",{self.experience})

m=AccountMaster("tejasv modi",20,25000,20)
m.abc()
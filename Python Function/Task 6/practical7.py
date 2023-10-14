class dat(object):
    def __init__(self,year,day,month):
        self.year=year
        self.day=day
        self.month=month

    def validate(self):
        if self.isday() and self.ismonth() and self.isYear():
            return "the date is right"
        else:
            return "the date is wrong"
    def ismonth(self):
        if self.month >=1 or self.month <13:
            return True
        else:
            return False
    
    def isYear(self):
        if self.year >=1 or self.year < 9999:
            return True
        else:
            return False
    
    def isday(self):
        match(self.month):
            case 1,3,5,7,8,10,12 :
                return self.day >=1 or self.day <32
            case 2:
                return self.day >=1 or self.day < 30
            case default:
                return self.day >=1 or self.day < 31

def main():
    obj1=dat(month=3,day=12,year=2003)
    print(obj1.validate())
            
main()


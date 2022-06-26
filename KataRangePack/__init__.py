

from sys import setswitchinterval

class RangeClass:
    def __init__(self, range):
        self.range = range
    
    firstInterval = str(range)[0]
    firstNo = str(range)[1:str(range).find(',')]
    secNo = str(range)[str(range).find(',') + 1: -1]
    secInterval = str(range)[-1]

    def range_validation(self):
        valid1 = (self.firstInterval == '(' or self.firstInterval == '[')
        valid2 = (self.secInterval == ')' or self.secInterval == ']')
        valid3 = (self.firstNo.isdigit() and self.secNo.isdigit())
        valid4 = (self.firstNo <= self.secNo)
        if(valid1 and valid2 and valid3 and valid4):
            return True
        else:
            return False


    def Contains(self, value):
        t1 = False
        var = range(self.first, self.last)
        for i in var:
            if(i == value):
                t1 = True
        return t1

    def GetAllPoints(self):
        result = ""
        var = range(self.first, self.last)
        for i in var:
            if i < self.last - 1 :
                result += str(i) + ","
            else:
                result += str(i)
        return result
    
    def EndPoints(self):
        return str(self.first) + "," + str(self.last-1)


    def Equals(self, other: 'RangeClass'):
        var1 = range(self.first, self.last)
        var2 = range(other.first, other.last)
        if(var1 == var2):
            return True
        else:
            return False

    def overlapsRange(self, other: 'RangeClass'):
        choice = False

        for i in range(self.first, self.last):
            for j in range(other.first, other.last):
                if(i == j):
                    choice = True
                else:
                    choice = False
        return choice

print(RangeClass("(1,2)").range_validation())
                


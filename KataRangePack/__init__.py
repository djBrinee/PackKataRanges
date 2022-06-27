from attr import s


class RangeClass:
    def __init__(self, range):
        self.range = range
    
    def split(self):
        firstInterval = self.range[0]
        firstNo = self.range[1:self.range.find(',')]
        secNo = self.range[self.range.find(',') + 1: -1]
        secInterval = self.range[-1]
        return [firstInterval, firstNo, secNo, secInterval]
    
    def range_validation(self):
        valid1 = (self.split()[0] == '(' or self.split()[0] == '[')
        valid2 = (self.split()[3] == ')' or self.split()[3] == ']')
        valid3 = (self.split()[1].isdigit() and self.split()[2].isdigit())
        valid4 = (int(self.split()[1]) <= int(self.split()[2]))
        if(valid1 == True and valid2 == True and valid3 == True and valid4 == True):
            return True
        else:
            return False
        
    def LenghtRange(self):
        L1 = int(self.split()[1])
        L2 = int(self.split()[2])
        if(self.split()[0] == '('):
            L1 += 1
        if(self.split()[3] == ']'):
            L2 += 1
        return range(L1, L2)

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




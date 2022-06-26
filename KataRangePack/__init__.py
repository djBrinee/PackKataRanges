

class RangeClass:
    def __init__(self, range):
        self.range = range
    
    firstInterval = range[0]
    firstNo = range[1:range.find(',')]
    secNo = range[range.find(',') + 1: -1]
    secInterval = range[-1]

    def range_validation(self):
        if(firstInterval == '(' or firstInterval == '['):
            answer = True



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
                


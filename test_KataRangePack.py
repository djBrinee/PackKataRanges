import pytest
from KataRangePack import RangeClass

obj1 = RangeClass("(2,3)")
obj2 = RangeClass("[2,5)")
obj3 = RangeClass("[3,6]")

def test_range_Validationobj1():
    assert obj1.range_validation() == True

def test_splitobj1():
    assert obj1.split() == ['(', '2', '3', ')']

def test_range_Validationobj2():
    assert obj2.range_validation() == True

def test_splitobj2():
    assert obj2.split() == ['[', '2', '5', ')']

def test_LenghtRange():
    assert obj2.LenghtRange() == range(2,5)
    
def test_LenghtRange2():
    assert obj3.LenghtRange() == range(3,7)

# def test_RangeContains():
#     assert c1.Contains(2) == True

# def test_GetAllPoints():
#     assert c1.GetAllPoints() == "2,3,4,5"

# def test_NoContain():
#     assert c2.Contains(100) == False
    
# def test_EndPoints():
#     assert c1.EndPoints() == "2,5"

# def test_Equals():
#     assert c1.Equals(c2) == True

# def test_notEquals():
#     assert c3.Equals(c4) == False

# def test_NotoverlapsRange():
#     assert c5.overlapsRange(c6) == False

# def test_overlapsRange():
#     assert c7.overlapsRange(c8) == True

# def test_overlapsRange1():
#     assert c7.overlapsRange(c7) == True

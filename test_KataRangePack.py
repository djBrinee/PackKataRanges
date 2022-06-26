import pytest
from KataRangePack import RangeClass

c1 = RangeClass(2, 6)
c2 = RangeClass(2, 6)
c3 = RangeClass(3, 7)
c4 = RangeClass(4, 5)
c5 = RangeClass(7, 10)
c6 = RangeClass(2, 5)
c7 = RangeClass(2, 10)
c8 = RangeClass(3, 5)

def test_RangeContains():
    assert c1.Contains(2) == True

def test_GetAllPoints():
    assert c1.GetAllPoints() == "2,3,4,5"

def test_NoContain():
    assert c2.Contains(100) == False
    
def test_EndPoints():
    assert c1.EndPoints() == "2,5"

def test_Equals():
    assert c1.Equals(c2) == True

def test_notEquals():
    assert c3.Equals(c4) == False

def test_NotoverlapsRange():
    assert c5.overlapsRange(c6) == False

def test_overlapsRange():
    assert c7.overlapsRange(c8) == True

def test_overlapsRange1():
    assert c7.overlapsRange(c7) == True

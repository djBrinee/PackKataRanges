import pytest
from KataRangePack import RangeClass

valid1 = RangeClass()
valid2 = RangeClass()

def test_range_Validation():
    assert RangeClass("(2,3)").range_validation() == True

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

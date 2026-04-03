import pytest

def test_equality():
    list1 = [1,2,3]
    list2 = [1,2,3]
    assert list1 == list2

## skip marker

@pytest.mark.skip
def test_comparison():
    assert 4<5

## skipif marker

@pytest.mark.skipif(False,reason="Not Greater")
def test_greater():
    assert 7>2

@pytest.mark.skipif(True,reason="Lesser")
def test_less():
    assert 5<6

@pytest.mark.parametrize("a,b,expected",[(2,3,5),(3,4,7),(4,5,9)])
def test_addition(a,b,expected):
    assert a+b==expected








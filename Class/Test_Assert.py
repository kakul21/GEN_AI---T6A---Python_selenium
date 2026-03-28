def test_equality():
    assert 4==4
    assert "4"=="4"
    assert "Hello"=="Hello"
    assert "Hello"!="Hii"

def test_comparison():
    assert 4<5
    assert 8>2
    assert 7>=4
    assert 4<=8

def test_membership():
    listt = ["Apple","Banana","Orange"]
    assert "Apple" in listt
    assert "BANANA" not in listt
    assert "ORANGE" != listt[0]
    assert "Apple" == listt[0]

def test_identity():
    assert 4 is 4
    assert 4 is not 5


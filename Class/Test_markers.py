import pytest

## TASK 2: Pytest Markers Practice

# Create 2 custom markers:
# @pytest.mark.smoke
# @pytest.mark.regression
# Write:
# 2 test cases for smoke
# 2 test cases for regression
# Each test should:
# Contain a simple assertion
# Run tests using:
# Only smoke tests
# Only regression tests

@pytest.mark.smoke
def test_equality():
    assert 4+1 == 5

@pytest.mark.smoke
def test_upper():
    assert "Task".upper() == "TASK"

@pytest.mark.regression
def test_membership():
    listt = ["Apple","Banana","Orange"]
    assert "Apple" in listt

@pytest.mark.regression
def test_multiplication():
    assert 3 * 3 == 9





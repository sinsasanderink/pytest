import addition
import pytest

def test_add():
    assert addition.add(4, 5) == 9

def test_sub():
    assert addition.sub(4, 5) == -1
    # use double : to run test on specific function, eg python3 -m pytest test_addition.py::test_add
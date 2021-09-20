from pythonisms import __version__
from pythonisms.pythonic import *

def test_version():
    assert __version__ == '0.1.0'
###################################################################################
def test_factors_1():
    actual = factors_one(10)
    expected = [1, 2, 5, 10]
    assert actual == expected

# testing our Module using pytest library
# pytest -> unit testing Framework
# pytest -> automate the process of running this tests & tell if there's an Error
from unit1 import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negetive():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")
    
    
# Run the following in the Terminal -> 
# python -m pytest "c:\Users\ariji\OneDrive\Desktop\Learn python\F. Unit Tests\testB_Unit1.py"
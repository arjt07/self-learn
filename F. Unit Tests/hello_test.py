from hello import hello

def test_default():
    assert hello("Arijit")  == "hello, Arijit"
    
def test_argument():    
    assert hello()  == "hello, world"
    
 
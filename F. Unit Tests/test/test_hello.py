from hello import hello

def test_default():
    assert hello("Arijit")  == "hello, Arijit"
    
def test_argument():    
    assert hello()  == "hello, world" 
    

# run pytest on test Folder ->
# python -m pytest "c:\Users\ariji\OneDrive\Desktop\Learn python\F. Unit Tests\test"
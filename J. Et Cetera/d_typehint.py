# type hint -> to check whether or not our variables are using the right type

def meow(n: int) -> str:
    # DocStrings -> Documenting our code
    """Meow n times

    Args:
        n (int): Number of times to meow

    Raise:
        TypeError: If n is not an int
        
    Returns:
        str: A string of n meows, one per line
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end = "")

# run in Terminal -> python -m mypy "c:\Users\ariji\OneDrive\Desktop\Learn python\J. Et Cetera\d_typehint.py"
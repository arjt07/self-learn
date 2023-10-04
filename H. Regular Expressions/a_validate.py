# Regular Expressions or regexes

# re library -> search for Patterns in input value
# patterns -> strings, f strings

# . -> any char except a new line, 
# sign -> no. of Repetation, * -> 0 or, more, + -> 1 or more, ? -> 0 or, 1
# {m} -> m, {m, n} -> m-n

# ^ -> matches the Start of the String, $ -> ...End ...String

# [] -> matches a set of characters, [^] -> compliment the Set(cann't match a set of char)
# [a-zA-Z0-9_.] => \w(word char. includes a-z, A-Z, 0-9, _)

# w -> word char, W -> not a word char, d -> decimal digit, D, s-> whitespace char, S

# a|b => a or b 
# ////////////////////////////////////////////////////////////////////

import re

email = input("what's your email? ").strip()

# r = raw String
# if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|in|edu)$", email, re.IGNORECASE):  
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|in|edu)$", email, re.IGNORECASE):  
    print("valid")
else:
    print("invalid")

 


# email = input("what's your email? ").strip()

# username, domain = email.split("@")

# if username and (domain.endswith(".com") or domain.endswith(".in")):
#     print("valid")
# else:
#     print("invalid")


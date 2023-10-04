# reformat the user input in the format we expect
# (...) -> a group capture, (?:...) -> non-capturing version
# r = raw String
import re

name = input("what's your name? ").strip()

# (:=) walrush operator -> assigning value & asking a Boolean question
if matches := re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups()
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
 


# name = input("what's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")


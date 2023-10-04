# MATCH
name = input("what's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Dreco":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Dreco":
        print("Slytherin")
    case _:       # Default case like Switch
        print("Who?")


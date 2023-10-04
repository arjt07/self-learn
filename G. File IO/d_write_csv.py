import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students_3.csv", "a", newline='') as file:
    # append = csv.writer(file)
    # append.writerow([name, home])
    append = csv.DictWriter(file, fieldnames=["name", "home"])
    append.writerow({"home": home, "name": name})
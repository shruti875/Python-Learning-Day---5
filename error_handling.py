# Common Python Errors
# ValueError
int("hello")

# TypeError
"10" + 5

# ZeroDivisionError
10 / 0

# FileNotFoundError
open("missing.txt", "r")

# IndexError
numbers = [1, 2, 3]
print(numbers[10])

# KeyError
student = {"name": "Adi"}
print(student["age"])

# Handling Errors
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number.")
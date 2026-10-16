# JSON = JavaScript Object Notation

# 6.a Importing JSON
import json

# 6.b Python Dictionary → JSON
student = {
    "name": "Adi",
    "age": 21,
    "course": "CSE"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# 6.c JSON → Python Dictionary
with open("student.json", "r") as file:
    student = json.load(file)

print(student)

# 6.d Important JSON Functions
# json.dump() → Python → JSON file
# json.load() → JSON file → Python
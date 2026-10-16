# writing a line
with open("data.txt" , "w") as file:
    file.write("Hello Python")

# Writing Multiple Lines
with open("data.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
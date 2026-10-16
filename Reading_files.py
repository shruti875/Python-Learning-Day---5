# to read an entire file
with open("data.txt" , "r") as file:
    data = file.read()
    print(data)

# to read one line
with open("data.txt" , "r") as file:
    line = file.readline()
    print(line)

# to read all line into a list
with open("data.txt" , "r") as file:
    lines = file.readlines()
    print(lines)
    
# reading using a loop
with open("data.txt" , "r") as file:
    for line in file:
        print(line)
file = open("data.txt" ,"x")   #to create a new file
file = open("data.txt" ,"w")    #to write a file
file = open("data.txt" , "r")     #to read a file
file = open("data.txt" ,"a")    #to add in file


# for closing a file

file.close()

# for opening a file

with open("data.txt" , "r") as file:
    data = file.read()
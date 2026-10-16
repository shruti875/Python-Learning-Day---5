
# Code that might produce an error:
# try:
#     number = int(input("Enter number: "))

# except
# Handles the error:
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number")


# c Multiple except
try:
    number = int(input("Enter number: "))
    result = 10 / number

except ValueError:
    print("Enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")


# else
# Runs when there is no error:
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print("Number:", number)


# finally
# Runs whether an error occurs or not.
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

finally:
    print("Program finished")
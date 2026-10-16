# Creating a Custom Exception
class InsufficientBalanceError(Exception):
    pass

# Using raise
balance = 500
amount = 1000

if amount > balance:
    raise InsufficientBalanceError("Insufficient balance")

# Handling Custom Exception
try:
    balance = 500
    amount = 1000

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")

except InsufficientBalanceError as e:
    print(e)
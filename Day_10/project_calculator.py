# Calculator 
from art import logo

print(logo)

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2


# Dictionary to choose operation

operation_dict = {
    "+" : add, 
    "-" : subtract,
    "*" : multiply,
    "/" : divide, 
}

num1 = float(input("What's the first number?: "))

for symbol in operation_dict:
    print(symbol)

operation_selected = input("pick an operation from the list above: ")
num2 = float(input("What's the second number?: "))

continue_calulation = True
while continue_calulation:

    calculation = operation_dict[operation_selected]
    answer = calculation(num1, num2)
    print(f"{num1} {operation_selected} {num2} = {answer}")

    more_calculations = input(f"Type 'y' to continue with {answer}, or type 'n' to exit: ")

    if more_calculations == "y":
        num1 = answer
        operation_selected = input("pick an operation: ")
        num2 = int(input("What's the next number?: "))
    elif more_calculations == "n":
        continue_calulation = False


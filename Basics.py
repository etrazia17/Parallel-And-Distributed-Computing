print("abc")

# Task-01
# Simple Calculator

def calculator():
    # Take user inputs
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (+, -, *, /): ")

    num1 = float(num1)
    num2 = float(num2)
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
    return f"The result is: {int(result) if result.is_integer() else result}"


print(calculator())

# Task-02
# List

# Creating a list
fruits = ["apple", "banana", "mango"]

# Accessing elements
print(fruits[0]) 





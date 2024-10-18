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

# Adding an element
fruits.append("orange")
print(fruits)  

# Removing an element
fruits.remove("banana")
print(fruits)  

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Tuple
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  

# Accessing elements in a tuple
print(my_tuple[0])  
print(my_tuple[2])  

# Concatenating tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2
print(combined)  

# Dictionary

# Creating a dictionary
person = {"name": "Ali", "age": 25}
print(person) 

# Adding a new key-value pair
person["city"] = "Karachi"
print(person)  

# Accessing a value
print(person["name"]) 













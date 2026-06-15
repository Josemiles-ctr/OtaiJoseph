# Calculator progrm with some error handling(Out of scope for this assigmnment)
def calculator():
    print("Choose the operation you want to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    try:
        operation = int(input("Operation (e.g 1 for Addition): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
    if operation not in [1, 2, 3, 4]:
        print("Invalid operation. Please choose a number between 1 and 4.")
        return
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    if operation == 1:
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == 2:
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == 3:
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == 4:
        result= divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")   
        
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return num1 / num2

calculator()
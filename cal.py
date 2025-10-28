# 🧮 Simple Python Calculator
# Author: [Your Name]
# Description: A lightweight command-line calculator for basic arithmetic operations.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("=== Simple Python Calculator ===")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation!"

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()

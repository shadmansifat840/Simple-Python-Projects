# Functions to built a calculator.

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y
    

# Printing a menu. 

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# main code.

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):

        # Taking input.

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == ('1'):
            print("Result:", add(num1, num2))
        elif choice == ('2'):
            print("Result:", subtract(num1, num2))
        elif choice == ('3'):
            print("Result:", multiply(num1, num2))
        elif choice == ('4'):
            print("Result:", divide(num1, num2))
    else:
        raise ValueError("Ivalid Input !!!")

    ano_cal = input("Do you want to perform another calculation? (yes = 1 /no = 0): ")
    if (ano_cal == '0'):
        break


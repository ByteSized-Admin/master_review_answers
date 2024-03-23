# Completed Assignment: Introduction to Conditionals in Python

# Question 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Question 2
if age >= 65:
    print("You are a senior citizen.")
elif age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Question 3
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Question 4
password_input = input("Enter the password: ")
password = "secret"
if password_input == password:
    print("Access granted.")
else:
    print("Access denied.")

# Question 5
letter = input("Enter a letter: ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

# Debugging Section - Corrected code

# Question 6
# Fixed: Added int conversion and fixed syntax error in if condition
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Question 7
# Fixed: Added missing colon, corrected comparison operator, and added missing colon after else
number = int(input("Enter a number: "))
if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")

# Question 8
# Fixed: Indentation for print statement under if condition
password = input("Enter the password: ")
if password == "PythonRocks":
    print("Access granted.")
else:
    print("Access denied.")

# Question 9
# Fixed: Logic in checking for vowels
letter = input("Enter a letter: ").lower()
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

# Question 10
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

if operation == "add":
    print(f"The result is {num1 + num2}")
elif operation == "subtract":
    print(f"The result is {num1 - num2}")
elif operation == "multiply":
    print(f"The result is {num1 * num2}")
elif operation == "divide":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result is {num1 / num2}")
else:
    print("Invalid operation")

# This completed script demonstrates how each question should be answered, including corrections for the debugging section.

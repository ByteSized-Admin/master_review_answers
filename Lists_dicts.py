# Completed Assignment: Exploring Lists and Dictionaries in Python

# Solutions to the questions

# Question 1
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Question 2
fruits.append("orange")
print(fruits)

# Question 3
for fruit in fruits:
    print(fruit)

# Question 4
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruit_colors)

# Question 5
fruit_colors["orange"] = "orange"
print(fruit_colors)

# Question 6
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}.")

# Debugging Section - Corrected code

# Question 7
fruits = ["apple", "banana", "cherry"]
# Fixed: Missing closing bracket and index out of range error
print(fruits[2])

# Question 8
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
# Fixed: Missing closing bracket and colon after for loop
for fruit in fruit_colors.keys():
    print(fruit)

# Question 9
# CHANGED

# Question 10
favorite_fruits = []
print("Enter your favorite fruits one at a time. Type 'done' to finish.")
while True:
    fruit = input()
    if fruit.lower() == "done":
        break
    favorite_fruits.append(fruit)
print("Your favorite fruits are:", favorite_fruits)

# QUESTION 10 CHECK :)

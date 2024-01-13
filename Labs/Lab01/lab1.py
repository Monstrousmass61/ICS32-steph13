# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Stephen Huang
# steph13@uci.edu  
# 42399418

import operator

print("Hello! This is my calculator for ICS 32.\n")
var1 = int(input("Enter your first variable: "))
var2 = int(input("Enter your second variable: "))
operate = input("Enter your desired operator (+, -, x, or %): ")

operate_dict = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "%": operator.mod
}

if operate not in ["+", "-", "x", "%"]:
    print('\nInvalid.')

else:
    print(f"\nThe result of your calculation is: {operate_dict[operate](var1, var2)}")
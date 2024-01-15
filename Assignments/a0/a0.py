# a0.py

# Starter code for assignment 0 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Stephen Huang
# steph13@uci.edu
# 42399418
user_input = int(input())
whole_str = ""
for num in range(user_input):
    space = "  " * num
    whole_str += f"+-+\n{space}| |\n{space}+-"
if user_input > 0:
    whole_str += "+"
print(whole_str)
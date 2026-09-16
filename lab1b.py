# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Melissa Aydin
# Date: 16 Sep 2026
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
#	Create another variable called "num2" and take its value from user. 
# Convert the values to integers using int() function
num1=input('please enter a number for the variable num1:')
num2=input('please enter a number for the variable num2:')
num1=int(num1)
num2=int(num2)
print(type(num1))
print(type(num2))
# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.

print("num1 + num2 =", num1 + num2)
print("num1 - num2 =", num1 - num2)
print("num1 * num2 =", num1 * num2)
print("num1 ** num2 =", num1 ** num2) 
print("num1 / num2 =", num1 / num2)
print("num1 // num2 =", num1 // num2)
print("num1 % num2 =", num1 % num2)
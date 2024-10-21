# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:12 2024

@author: fabiola patero
"""
#Exercise 3

name = input("Please enter your name: ")
hometown = input("Please enter your hometown: ")
age_input = input("Please enter your age: ")

# Store the information in a dictionary
user_info ={
    "name": name, 
    "hometown": hometown, 
    "age": age_input, 
    }


# Print the values on separate lines
print("In". join(user_info.values()))

# Check if age is a number
try:
    age = int(age_input)
except ValueError:
    print("Invalid age input. Please enter a valid integer for age.")

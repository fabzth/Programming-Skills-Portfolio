# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:16 2024

@author: fabiola patero
"""

#Exercise 10


def check_even_odd(number):
    """Function to determine if a number is even or odd."""
    if number % 2 == 0: 
        return f"{number} is even." 
    else:
        return f"{number} is odd."
    
def main():
    
    user_input = input("Enter a number: ") 
    
    try: 
        
        number = int(user_input) 
        
        result = check_even_odd (number) 
        
        print(result) 
    except ValueError: 
        print("Please enter a valid integer.")

if __name__== "__main__":
    main()
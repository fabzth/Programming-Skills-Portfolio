# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:46:07 2024

@author: fabiola patero
"""
#Exercise 6 


password= "sigma"
max_attempts= 5
attempts=0

while attempts< max_attempts:
    password= input("Please enter your password")

    if password== password:
        print("You now have access!")
        break
    else:
        attempts +=1
        remaining_attempts= max_attempts - attempts
        print(f"Incorrect password. You hve {remaining_attempts} attempts(s)")

if attempts== max_attempts:
    print("Maximum attempts reached. Please try again another time.") 
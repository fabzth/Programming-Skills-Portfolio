# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:15 2024

@author: fabiola patero
"""

#Exercise 8

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Option to input search term
search_term = input("Enter a name to search for: ")

if search_term in names: 
    print(f"{search_term} is in the List.")
else: 
    print(f"{search_term} is not in the list.") 

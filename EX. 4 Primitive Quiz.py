# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:13 2024

@author: fabiola patero
"""
#Exercise 4

# Define a dictionary with countries and their capitals
question = {"France":"Paris"}


# Function to conduct the quiz
def run_quiz (questions):
    for country, capital in questions.items():
        answer = input(f"What is the capital of {country}? ").strip()
        if answer. lower () == capital.lower():
            print( "Great job!")
        else:
            print("wrong anser, answer is (capital}.")
         
# Start the quiz
run_quiz (question)
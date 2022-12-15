# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:57:06 2020

@author: minne
"""
import random

def user_guess():
    number = random.randint(1,10)
    
    prompt = input("Pick a number between 1 and 10: ")
    prompt = int(prompt)
    guess = 0
    
    while guess < 4:
        if number == prompt:
            print("Correct!")
            break
        elif abs(number-prompt)>5:
            print("Not even close.")
            guess += 1
        elif abs(number-prompt)>=3 and abs(number-prompt)<=5:
            print("Close.")
            guess += 1
        elif abs(number-prompt)<3:
            print("Almost there.")
            guess += 1
            
        prompt = input("Pick a number between 1 and 10: ")
        prompt = int(prompt)
        
    else:
        print("Out of chances, goodbye.")
        
def comp_guess():
    li=[1,2,3,4,5,6,7,8,9,10]
    lowest = 0
    highest = 9
    guess = 0
    
    while guess < 3:
        mid = (lowest+highest)//2
        shot = li[mid]
        print("Is your number",shot)
        response = input("Tell me if its, too big, too small, or correct: ")
        
        if response == "correct":
            print("Gotcha! Smd.")
            break
        
        elif response == "too big":
            highest = mid - 1
            
        elif response == "too small":
            lowest = mid+1
            
        guess += 1
        
    else:
        print("Oh no I failed.")


        
    
    
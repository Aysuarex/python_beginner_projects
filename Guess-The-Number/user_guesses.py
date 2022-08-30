from itertools import count
import random

"""
The user attempts to guess the computer's number and the computer 
indicates whether it is correct or not. This continues until the number is gotten.
"""

def guess(x):
    number = random.randint(1, x)

    guess = int(input(f"\nGuess a number from 1 to {x}: "))

    count = 0 #This counts the number of guess attempts
    while guess != number:
        if guess > number:
            guess = int(input("Too High. Try again: "))
            count+=1
        elif guess < number:
            guess = int(input("Too low, Try again: "))
            count+=1
    
    print(f"Congrats! You have guessed the number {number} correctly! It took {count} attempts.")

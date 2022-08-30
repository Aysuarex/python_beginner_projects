import random

"""
The computer attempts to guess the users's number and the user
indicates whether it is correct or not. This continues until the computer correctly guesses the number.
"""

def guess(x):
    l = 1 #lower boundary of guesses
    number = 0
    
    while (number <1 or number>x):
        number = int(input(f"\nInput a secret number from 1 to {x}: "))
    
        if number <1 or number > x:
            print(f"Your secret number should be between 1 and {x}")

    guess = 0 #This initialises the variable for the loop
    
    count = 0 #This counts the number of guess attempts
    while guess != number:
        if l == x: #randint doesnt work if the lowerboundary == upperboundary
            guess = l #could also be x b/c l = x
        else:
            guess = random.randint(l, x)
            print(f"computer's guess = {guess}")
            count+=1
        if guess == number:
            break

        result = ' '
        while (result != 'h' and result != 'l'):
            result = input(f"\nIs {guess} too High (H) or too Low (L)? ").lower()
            if result == 'h':
                x = guess - 1
            elif result == 'l':
                l = guess + 1
            else:
                print("Erroneous input! Try again")

    print(f"\nYay! The computer guessed your number {number} correctly! It took {count} attempts")

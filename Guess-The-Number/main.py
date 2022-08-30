import user_guesses, computer_guesses

"""
Program that runs the guess-the-number game
"""

if __name__ == "__main__":
    x = 0 #This initialises the upper boundary for the loop
    while (x < 10 or x > 100000):
        try:
            print("\nWelcome to Guess-The-Number")
            x = int(input("Input an upper limit between 10 and 100,000: "))
        except ValueError:
            print('Error! The number needs to be an integer')
        
        if x < 10 or x > 100000:
            print("Error! The value should be between 10 and 100,000")

    choice = ' ' 
    while (choice != 'a' and choice != 'b'):
        choice = input("\nHow do you wish to play?\n\
A. Player guesses computer's number\n\
B. Computer guesses player's number.\n\t\t==> ").lower()

        if choice == 'a':
            user_guesses.guess(x)
        elif choice == 'b':
            computer_guesses.guess(x)
        else:
            print("Wrong choice, pick again")

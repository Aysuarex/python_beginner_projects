import random
import time
"""
A basic game of rock paper scissors against the computer.
"""

def main():
    reply = 'Y'
    while reply in ['Y', 'N']:
        print("\nWhat's your choice?")

        user = 0 #This initialises variabe 'user' for the loop
        while (user != 'r' and user != 'p' and user != 's'):
            user = input("'r' for rock, 'p' for paper and 's' for scissors\n\t\t==> ").lower()
            if user != 'r' and user != 'p' and user != 's':
                print("Invalid choice! Try again\n")
        
        computer = random.choice(['r', 'p', 's'])
        print("Computer chose "+computer, end='\n\n')

        if user == computer:
            print ("It's a tie!\n")
        
        # r > s, s > p, p > r
        if is_win (user, computer):
            print ("You Win!\n")
        elif is_win (computer, user): #This line is not necessary
            print ("You Lose!\n")
        reply = input("Do you wish to play again?(Y/N): ").upper()
        if reply == 'N':
            print('Bye! Come back soon')
            break           
            

def is_win(player, opponent):
    #retun true if player wins
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')):
        return True

print(main())

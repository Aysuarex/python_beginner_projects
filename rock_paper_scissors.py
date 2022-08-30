import random
"""
A basic game of rock paper scissors against the computer.
"""

def play():
    print("\nWhat's your choice?")

    user = 0 #This initialises variabe 'user' for the loop
    while (user != 'r' and user != 'p' and user != 's'):
        user = input("'r' for rock, 'p' for paper and 's' for scissors\n\t\t==> ").lower()
        if user != 'r' and user != 'p' and user != 's':
            print("Invalid choice! Try again\n")
    
    computer = random.choice(['r', 'p', 's'])
    print("Computer chose "+computer, end='\n\n')

    if user == computer:
        return ("It's a tie!")
    
    # r > s, s > p, p > r
    if is_win (user, computer):
        return "You Win!"
    elif is_win (computer, user): #This line is not necessary
        return ("You Lose!")

def is_win(player, opponent):
    #retun true if player wins
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r')):
        return True

print(play())
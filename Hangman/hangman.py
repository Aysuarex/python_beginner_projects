import random
import time
from words import word_list

"""
Hangman game
"""

def get_word():
    word= (random.choice(word_list)).upper()
    return word #.upper()

def play(word):
    word_completion = '_' * len(word) #prints the word as underscores (_____)
    guessed = False #Has the word been correctly guessed yet?
    guessed_letters = [] #letters that have been guessed
    guessed_words = [] #words that have been guessed
    lives = 6 #number of remaining trials which corresponds to the diagrams

    print("\nWelcome to Hangman")
    print(diagram)
    print(word_completion)
    print("\n")

    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        # if a letter (which must be in the english alphabet) was guessed
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess} earlier")
            elif guess not in word:
                print(f"{guess} is not in the word")
                lives -= 1
                guessed_letters.append(guess)
            else: # letter was guessed correctly
                print("Good job! {guess} is in the word")
                guessed_letters.append(guess)
                
                # convert the string to a list so we can index it and edit the contents
                word_as_list = list(word_completion)
                
                # find all the indices which the guessed letter occupies 
                # in the word and make a list out of them
                indices = [i for i,letter in enumerate(word) if letter == guess]
                
                # interating through the list and replacing the '_' in the original 
                # word_completion variable with the appropriate guessed letter
                for index in indices:
                    word_as_list[index] = guess
                    
                    # convert the list back to a string for printing
                    word_completion = "".join(word_as_list)

                # if the last correct guess completed the word
                if '_' not in word_completion:
                    guessed = True
        
        # if the guess was a word having the right length
        # (with all its letters within the alphabet)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess} earlier")
            elif guess != word:
                print(f"{guess} is not the word")
                guessed_words.append(guess)
            else: # whole word was guessed correctly
                guess = True
                word_completion = word

        # if the guess was neither a letter in the alphabet, 
        # nor a word with the appropriate length
        else: 
            printf("Error! Invalid Guess. Try again")
        
        print(diagram(lives))
        print(word_completion)
        print("\n")
    
    if guessed: #user guesses the word correctly
        print(f"Congrats! You guessed the word correctly with {lives} lives left. You Win!")
    else: #user runs out of lives but couldnt guess correctly
        print("Sorry, you ran out of tries. The word was {word}. Maybe next time!")


def diagram(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
                """
    ]
    return stages[lives]

def main():
    get_word()
    play(word)

    while input("Do you wish to play again?(Y/N): ").upper() == 'Y'
        get_word()
        play(word)
    print("Bye! Come Back Soon.")

if __name__ == "__main__":
    main()

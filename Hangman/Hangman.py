# Make a Hangman Game
# Completed

import os
import random
from Hangman_art import stages,logo
from Hangman_words import words

x=random.randint(0,len(words)-1)
chosen_word=words[x]

display=[]
guess=[]
total_guess=[]
# Initial Display
clear_screen()
print("Welcome to hangman corporated, try not to die.")
print(logo)
print(stages[-1])
print(f"You word has {len(chosen_word)} letters.")
for i in range(len(chosen_word)):
    display.append("_")
    guess.append("_")
display = ' '.join(display)
print(display)

# ANSI escape codes to underline text
def underline(text):
    return f"\033[4m{text}\033[0m"

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')

lives=6

while lives > 0:
    # User input
    print(f"\nYou have {lives} life\lives left.")
    input_letter=input("Guess a letter: ").lower()
    # Account for guessed letters
    if input_letter in total_guess:
        print("You guessed that already, try again.")
    else:
        # Add guess to total guessed letters
        total_guess.append(input_letter)
        # Check if guess is in the word
        if input_letter in chosen_word:
            # Account for multiple positions
            for i in range(len(chosen_word)):
                # Matching letter chek
                if input_letter == chosen_word[i]:
                    # Replace space in guessed input array
                    if guess[i]!=input_letter:
                        guess.pop(i)
                        guess.insert(i, input_letter)
        else:
            # Remove life if not a part of word
            if lives>0:
                print("\nNot a part of the word.\nYou lost a limb.")
                # Show how far gone (dead)
                print(stages[lives-1])
            lives-=1
        # Display guessed and unguessed
        print()    
        for i in range(len(guess)):
            print(underline(guess[i]),end=" ")
        print()    
        complete_guess = ''.join(guess)
        # Game Completion/End conditions
        if complete_guess == chosen_word:
            clear_screen()
            print("\nMission Accomplished. Good job!")
            print(f"The word was {chosen_word}")
            break
        if lives == 0:
            clear_screen()
            print("You ran out of lives! *Dies*")
            print(f"The word was {chosen_word}")


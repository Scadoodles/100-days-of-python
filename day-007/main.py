import os
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Generate a word and the blank word holder
word_list = ["ardvark", "baboon", "camel", "duck", "elephant", "falcon", "giraffe", "hippopotamus", "iguanq", "jaguar", "kangaroo", "leapard", "manatee", "narwhal", "ostrich", "porcupine", "quail", "rabbit", "squirrel", "turkey", "walrus", "zebra"]
chosen_word = random.choice(word_list)
blank_word = ["_"] * len(chosen_word)
user_lives = 6

while user_lives is not 0:
  os.system("cls||clear")
  
  #print the game state
  print(stages[user_lives])
  print(" ".join(blank_word))
  print("\n")

  # Is the word complete?
  user_word = "".join(blank_word)
  if user_word == chosen_word:
    # Yes - Victory game over
    print("Congratulations - You Win")
    break
  else:
    if user_lives is 1
      print("1 guess remaining.")
    else:
      print(f"{user_lives} guesses remaining.")

    # Ask the user to guess a letter
    user_letter = input("Guess a letter? ").lower()

  # Is the guessed letter in the word?
  if user_letter in chosen_word:
    # Yes - Fill in the word
    for index in range(0, len(chosen_word)):
      if user_letter == chosen_word[index]:
        blank_word[index] = user_letter
  else:
    # No
    # Player loses a life
    user_lives -= 1

    # Is the player out of lives ?
    if user_lives is 0:
      # Yes - Game over
      print("You're Out of Lives - Game Over")

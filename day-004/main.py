rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
art = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]
choices_index = ["r", "p", "s"]

# A matrix of game possibilities
# First index represents the user's choice
# Second index represents the game's choice
# True - user wins, False user loses, None - tie
games = [
  [None, False, True],
  [True, None, False],
  [False, True, None]
]

# The same matrix with text based messages
results = [
  [
    "Rock matches rock. Tie.",
    "Paper covers rock. You Lose.",
    "Rock smashes scissors. You Win."
  ], [
    "Paper covers rock. You Win.",
    "Paper matches paper. Tie.",
    "Scissors cut paper. You Lose."
  ], [
    "Rock smashes scissors. You Lose.",
    "Scissors cut paper. You Win.",
    "Scissors matches scissors. Tie"
  ]
]

# End game replay loop
def end():
  again = input("\r\nPlay again? (y/n) ").lower()
  if again == "y":
    print("")
    game()

def user_input():
  # get user input
  try:
    input_string = input("\r\nChoose your weapon: (r)ock, (p)aper, or (s)cissors: ").lower()
    choice = choices_index.index(input_string[0])
  except:
    print("\r\nInvalid User Input\r\n")
    return None
  return choice

def game():
  #start
  print("Let's play rock, paper, scissors!")

  user_choice = None
  while user_choice is None:
    user_choice = user_input()

  # get random game choice
  game_choice = random.randint(0, 2)
  
  print(f"\r\n{choices[user_choice]} VS ...\r\n")
  print(art[game_choice])
  print(f"\r\n{results[user_choice][game_choice]}")
  end()

game()

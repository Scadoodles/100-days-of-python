#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# gonna skip input validation for this one
# that's sorta out of scope even though it should be included
# should also always start with a letter
# but there's nothing forcing the user to choose at least 1 letter

import random

pwd_chars = []

for letter in range(0, nr_letters):
  pwd_chars.append(random.choice(letters))

for number in range(0, nr_numbers):
  pwd_chars.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
  pwd_chars.append(random.choice(symbols))

random.shuffle(pwd_chars)

print(f"\r\nHere is your new password: {''.join(pwd_chars)}")

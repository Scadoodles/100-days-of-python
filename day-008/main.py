import art
import os

os.system('cls||clear')
print(art.logo)

user_continue = True
symbols = [' ', '.', ',', '!', '?', '@', '#', '$', '%', '&', '*', '/', '-', '+', '_', '=', '(', ')', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = symbols + numbers + letters
alphabet_length = len(alphabet)

def shift_text(text, shift):
  shifted_text = ''
  for i in range(0, len(text)):
    letter_index = alphabet.index(text[i])
    letter_shift_index = (letter_index + shift) % alphabet_length
    letter = alphabet[letter_shift_index]
    # print(f"{i}, {text[i]}, {letter}")
    shifted_text += letter
  return shifted_text

def encrypt(text, shift):
    print(f"The encoded text is: {shift_text(text, shift)}")

def decrypt(text, shift):
  print(f"The decoded text is: {shift_text(text, 0 - shift)}")

def caesar():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction[0] == "e":
    encrypt(text, shift)

  if direction[0] == "d":
    decrypt(text, shift)

while user_continue is True:
  caesar()

  user_continue = input('Would you like to continue? (y/n): ').lower().strip() == 'y'

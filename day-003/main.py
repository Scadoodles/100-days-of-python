print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
''')
def die(message):
  print(f"\r\n{message}")
  print("You died.")
  again = input("\r\nPlay again? (y/n) ").lower()
  if again == 'y':
    game()
  exit()

def game():
  print("\r\nWelcome to Treasure Island.")
  print("Your mission is to find the treasure.") 

  print("\r\nYou encounter a fork in the road.")
  choice = input("Do you go 'left' or 'right'? ").lower()

  if choice != "right":
    die("You fall into a giant pit of spikes")

  print("\r\nYou find yourself standing at the edge of a large lake.")
  choice = input("Do you wait for a 'boat' or 'swim' across? ").lower()

  if choice != "boat":
    die("A swarm of pirahnas eat you alive!")

  print("\r\nYou arrive at a boathouse with 3 doors.")
  choice = input("Do you open the 'red', 'green', or 'blue' door? ").lower()

  if choice == "red":
    die("The a massive explosion comes from behind the red door as you open it.")
  elif choice == "green":
    die("The green door disolves into acid and pours all over you you.")
  elif choice != "blue":
    die("Your indecision leaves you in a frozen state of fear.")
  else:
    print("\r\nYou open the door to room full of glistening treasure!")
    print("\r\nCongratulations! Thanks for playing!")

game()

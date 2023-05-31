##print("test")
import requests


URLfirstgen = "https://pokeapi.co/api/v2/generation/1/"
URLdefaultpoke = "https://pokeapi.co/api/v2/pokemon-species/"


#x = requests.get(URLprice + random.randint(a,b))

##welcome user 
print("Welcome to the Pokedex!\n")
##creating list of valid options - they can pick random, by number, or name
valid_menu_choice = ["random", "number", "name", "by number", "by name", "1", "2", "3", "quit"]
choice = input("You can view a random pokemon, or pick one by their name or number. \n\n   What would you like to do? \n [RANDOM] [BY NAME] [BY NUMBER] ")
valid_choice = False

##force valid input to console 
while valid_choice == False:
  ##if it's only text, turn it into all lowercase to make sure its a valid input
  if choice.isalpha():
    choice = choice.lower()
  if choice not in valid_menu_choice:
    print("That's not a valid input.\n\n")
    choice = input("What would you like to do? \n [RANDOM] [BY NAME] [BY NUMBER] ")
    continue
  else: 
    if choice == "random" or choice == "1":
      choice = "random"
      print("\nYou selected random.")
    elif choice == "name" or choice == "by name" or "2":
      choice = "name"
      print("\nYou selected by name.")
    elif choice == "number" or choice == "by number" or choice == "3":
      choice = "number"
      print("\nYou selected by number.")
    else: 
      print("Thank you for using the pokedex!")
      break
    valid_choice = True

  if choice == "random": 
    print("do stuff here")
  elif choice == "name":
    name = input("What is the pokemon's name?")
    
    print("do stuff here")
  else: 
    print("do stuff here")
  
    

  

print("Your random Pokémon is: ")





print("test")
import requests


URLfirstgen = "https://pokeapi.co/api/v2/generation/1/"
URLdefaultpoke = "https://pokeapi.co/api/v2/pokemon-species/"


#x = requests.get(URLprice + random.randint(a,b))

##welcome user 
print("Welcome to the Pokedex!")
##creating list of valid options - they can pick random, by number, or name
valid_menu_choice = ["random", "number", "name", "by number", "by name", "1", "2", "3", "quit"]
choice = input("You can view a random pokemon, or pick one by their name or number. \n   What would you like to do? \n [RANDOM] [BY NAME] [BY NUMBER] ")
valid_choice = False

while valid_choice == False:
  if isalpha(choice):
    choice = choice.lower()
  if choice not in valid_menu_choice:
    print("That's not a valid input.")
    choice = input("What would you like to do? \n [RANDOM] [BY NAME] [BY NUMBER] ")
    continue
  else: 
    if choice == "random" or choice == "1":
      print("You selected random.")
    elif choice == "name" or choice == "by name" or "2":
      print("You selected by name.")
    elif choice == "number" or choice == "by number" or choice == "3":
      print("You selected by number.")
    else: 
      print("Thank you for using the pokedex!")
      break
  
    

  
if 
print("Your random Pokémon is: ")





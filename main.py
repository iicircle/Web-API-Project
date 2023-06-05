##print("test")
import requests
import random




#Code Graveyard
#to chose a random pokémon from the first generation
#gen1int = random.randint(1, 151)
#URLrandomGen = "https://pokeapi.co/api/v2/pokemon/" + str(gen1int) + "/"
#randGen = requests.get(URLrandomGen)
#data = randGen.json()
#print(data["name"].capitalize())
#URLdefaultpoke = "https://pokeapi.co/api/v2/pokemon-species/"

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
      
    elif choice == "name" or choice == "by name" or choice == "2":
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
    #random integer for a random pokemon from all gens
    genInt = random.randint(1, 1010)
    URLrandomGen = "https://pokeapi.co/api/v2/pokemon/" +     str(genInt) + "/"
    #To pull random Pokémon from API
    randGen = requests.get(URLrandomGen)
    data = randGen.json()
    print("Your random Pokémon is " +     data["name"].capitalize() + "! ID: " + str(data["id"]))

    #More options for the Pokémon
    learn = input("Would you like to learn more about this Pokémon? [yes, no] ")
    
    if learn.lower() == "yes":
      learning = input("What would you like to learn? [type, moves] ")
      if learning == "type":
        print("Here are the types of " + data["name"].capitalize())
        for type in data["types"]:
          print(type["type"]["name"].capitalize())
      if learning == "moves":
        print("Here are the moves that " + data["name"].capitalize() + " can learn!")
        for move in data["moves"]:
          print(move["move"]["name"].capitalize())
    else: 
      print("Alright... :(")

   
  ##select pokemon by name
  elif choice == "name":
    name = input("What Pokémon would you like by name?")
    URLnameGen = "https://pokeapi.co/api/v2/pokemon/" +     str(name) + "/"
    
    
    print("do stuff here")
  ##select pokemon by number
  elif choice == "number": 
    poke_number = input("What is the number of the pokemon? ")
    ##force valid numeric input
    while not poke_number.isnumeric():
      print("Sorry, that is not a valid input. Please try again.")
      poke_number = input("What is the number of the pokemon?")

    URLrandomGen = "https://pokeapi.co/api/v2/pokemon/" +     str(poke_number) + "/"
    #To pull Pokémon from index # from API
    randGen = requests.get(URLrandomGen)
    data = randGen.json()

    print("Your selected Pokémon is " +     data["name"].capitalize() + "! ID: " + str(data["id"]))
    
  
    

  







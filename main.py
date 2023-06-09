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



##function to generate a display box for pokemon
def Display_Pokemon(poke_id_num):
  URLpokemon = "https://pokeapi.co/api/v2/pokemon/" +     str(poke_id_num) + "/"
  pokeGen = requests.get(URLpokemon)
  data = pokeGen.json()
  ##get length of pokemon nam + id 
  text_width = len(str(data["name"]) + str(data["id"]))
  bracket_list = []
  bracket_list.clear()
  ## create bracket
  if text_width + 5 >= 18:
    bracket_width = text_width + 5
  else: 
    bracket_width = 18
  text_space_availible = bracket_width - (text_width + 5) ##space on side 
  if text_space_availible%2==1: ##if odd -> + 1 to bracket and sides
    bracket_width += 1 
    text_space_availible += 1  
  half_txt_space = int(text_space_availible/2)
  ##print basic lines 
  bracket_list.append("*"*(bracket_width)) ##generate flat line (l0)
  bracket_list.append("*" + (" "*(bracket_width-2)) + "*") ##edge w/ no text (l1)
  bracket_list.append("*" + (" "*half_txt_space) + str(data["name"]).upper() +  " [" + str(data["id"]) + "]" + (" " *half_txt_space) + "*") ## line for poke info (l2)
  for type in data["types"]:
    text_width = len(type["type"]["name"]) + 2  ##len of text
    half_txt_space = int((bracket_width - text_width)/2) ##space on side
    bracket = "*" + (" "*(half_txt_space-1)) + ">" + str(type["type"]["name"]).capitalize() + "<" + (" "*(half_txt_space-1))
    if len(bracket) + 1 != bracket_width:   #add a spot if != to bracket line 
      bracket += " "
    bracket_list.append(bracket + "*")


  printing_order = [0, 1, 1, 2]## to condense down printing list 
  i = 2
  for type in data["types"]: 
    printing_order.append(i+1)
    i += 1
  printing_order.append(1)
  printing_order.append(1)
  printing_order.append(0)
  print("")
  for i in range(len(printing_order)):
    print(bracket_list[printing_order[i]])
  print("")


def Learn_More_Pokemon():
  learning = input("What would you like to learn? [abilities, moves, weight] ")
  if learning == "abilities":
    print("Here are the ability or abilities that " + data["name"].capitalize() + " has!")
    for ability in data["abilities"]:
      print(ability["ability"]["name"].capitalize())
  if learning == "moves":
    print("Here are the moves that " + data["name"].capitalize() + " can learn!")
    for move in data["moves"]:
      print(move["move"]["name"].capitalize())
  if learning == "weight":
    print(data["name"].capitalize() + " is " + str(data["weight"]) + " hectograms!")


##welcome user 
print("Welcome to the Pokedex!\n\nYou can view a random pokemon, or pick one by their name or number.\n")
##variable to keep program in while loop 
poke_program_active = True
while poke_program_active:
  
  ##creating list of valid options - they can pick random, by number, or name
  valid_menu_choice = ["random", "number", "name", "by number", "by name", "1", "2", "3", "quit"]
  choice = input("\n   What would you like to do? \n [RANDOM] [BY NAME] [BY NUMBER] ")
  menu_choice = False

  ##this while loop runs if a menu selection has not been made 
  while menu_choice == False:
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
        #print("\nYou selected random.")
        
      elif choice == "name" or choice == "by name" or choice == "2":
        choice = "name"
        #print("\nYou selected by name.")
  
      elif choice == "number" or choice == "by number" or choice == "3":
        choice = "number"
        #print("\nYou selected by number.")
      else: 
        print("Thank you for using the pokedex.")
        poke_program_active = False
        break
    menu_choice = True
    

  
  if choice == "random": 
    #random integer for a random pokemon from all gens
    genInt = random.randint(1, 1010)
    URLrandomGen = "https://pokeapi.co/api/v2/pokemon/" +     str(genInt) + "/"
    #To pull random Pokémon from API
    randGen = requests.get(URLrandomGen)
    data = randGen.json()
    print("\nYour random Pokémon is " +     data["name"].capitalize() + "! ID: " + str(data["id"]))
    poke_number = genInt 
    Display_Pokemon(poke_number)
    #More options for the Pokémon
    learn = input("\nWould you like to learn more about this Pokémon? [yes, no] ")
      
    if learn.lower() == "yes":
      Learn_More_Pokemon()
    else: 
      print("Alright... :(")
      keep_using = input("\nWould you like to keep using the Pokédex? [yes, no]")
      if keep_using == "yes":
        menu_choice = False
        continue
      else:
        print("\n\nThank you for using the pokedex!")
        poke_program_active = False
        break

   
  ##select pokemon by name
  elif choice == "name":
    name = input("\nWhat Pokémon would you like by name?")

    URLnameGen = "https://pokeapi.co/api/v2/pokemon/" +     str(name) + "/"
    randGen = requests.get(URLnameGen)
    data = randGen.json()
    poke_number = data["id"]
    print("The Pokémon you selected is " +     data["name"].capitalize() + "! ID: " + str(data["id"]))
    Display_Pokemon(poke_number)

    learn = input("Would you like to learn more about this Pokémon? [yes, no] ")
    
    if learn.lower() == "yes":
      Learn_More_Pokemon()
    else: 
      print("Alright... :(")
      
    keep_using = input("Would you like to keep using the Pokédex? [yes, no]")
    if keep_using == "yes":
      menu_choice = False
      continue
    else:
      print("\n\nThank you for using the pokedex!")
      poke_program_active = False
      break
    

  ##select pokemon by number
  elif choice == "number": 
    poke_number = input("\nWhat is the number of the pokemon? ")
    ##force valid numeric input
    while not poke_number.isnumeric():
      print("Sorry, that is not a valid input. Please try again.")
      poke_number = input("What is the number of the pokemon?")

    URLidGen = "https://pokeapi.co/api/v2/pokemon/" +     str(poke_number) + "/"
    #To pull Pokémon from index # from API
    idGen = requests.get(URLidGen)
    data = idGen.json()

    print("\n\nThe Pokémon you selected is " +     data["name"].capitalize() + "! (ID: " + str(data["id"])+ ")")
    Display_Pokemon(poke_number)

    learn = input("\nWould you like to learn more about this Pokémon? [yes, no] ")
    
    if learn.lower() == "yes":
      Learn_More_Pokemon()
    else: 
      keep_using = input("\nWould you like to keep using the Pokédex? [yes, no]")
      if keep_using == "yes":
        menu_choice = False
        continue
      else:
        print("\n\nThank you for using the pokedex!")
        poke_program_active = False
        break
      
  keep_using = input("\nWould you like to keep using the Pokédex? [yes, no]")
  if keep_using == "yes":
    menu_choice = False
    continue
  else:
    print("\n\nThank you for using the pokedex!")
    poke_program_active = False
    break
    
  
    

  






  
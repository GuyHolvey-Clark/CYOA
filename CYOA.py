import random
yes_no = ["yes", "no"]
directions = ["north", "south", "east", "west"]
fight_flee = ["fight", "flee"]
global player_hp
player_hp = 30

def dice_roll(sides):
  roll = random.randint(1, sides)
  return roll

def intro():
    
    print("You awaken in a dimly lit forest, the air thick with an ancient aura.")
    print("A path leads forward, beckoning you towards the unknown.")
    print("Do you dare venture into the depths of this mysterious forest?")
    
    response = ""
    while response not in yes_no:
      response = input("yes/no: ")
      print("\n")
      if response == "yes":
        print("With a determined heart, you step onto the foreboding path.")
        room_1()
      elif response == "no":
        print("Fear grips you, and you remain lost in the shadows of the forest.")
        quit()
      else:
        print("I didn't understand that. Try again\n")

def room_1():
    
    print("The path splits into four directions, each leading into a different part of the forest.")
    print("To the north lies a dense thicket, to the east a shimmering lake, to the south a crumbling ruin, and to the west a towering mountain peak.")
    print("Which direction do you choose?")
    
    response = ""
    while response not in directions:
      response = input("north/east/south/west: ")
      print("\n")
      if response == "north":
          print("You brave the dense thicket, twigs and thorns scratching your skin.")
          room_2()
      elif response == "east":
          print("You approach the shimmering lake, its surface reflecting the dappled sunlight.")
          room_3()
      elif response == "south":
          print("You cautiously enter the crumbling ruin, its walls crumbling around you.")
          room_4()
      elif response == "west":
          print("You begin your ascent of the towering mountain peak, the wind whipping against your face.")
          room_5()
      else:
        print("I didn't understand that. Try again\n")

def room_2():
    print("You emerge from the thicket into a clearing, where a huge monster stands before you.")
    print("It resembles a large wolf, but its fur is as black as night and its eyes glow with an eerie red light.")
    print("Do you wish to fight the monster?")

    response = ""
    while response not in yes_no:
      response = input("yes/no: ")
      print("\n")
      if response == "yes":
          print("You draw your weapon and prepare to battle the monster.")
          monster_battle(15)
          room_1()
      elif response == "no":
          print("You turn and run, hoping to escape the creature's clutches.")
          room_1()
      else:
        print("I didn't understand that. Try again\n")


def room_3():
    print("As you approach, a hand emerges from the water, beckoning you closer.")
    print("Do you follow the hand's beckoning or remain on the shore?")

    response = ""
    while response not in yes_no:
      response = input("yes/no: ")
      print("\n")
      if response == "yes":
        print("You cautiously reach out and grasp the hand, which pulls you into the depths of the lake.")
        room_6()
      elif response == "no":
        print("You decide against following the hand and turn away from the lake.")
        room_1()
      else:
        print("I didn't understand that. Try again\n")

def room_4():
    print("The ruins are too dangerous to proceed. You turn around and head back to the forest.")
    print("\n")
    room_1()

def room_5():
    print("The mountain path is steep and dangerous. Despite your valiant efforts the way is impassable.")
    print("You turn around and head back to the forest.")
    print("\n")
    room_1()

def room_6():
    print("You find yourself in an underwater cavern, illuminated by an ethereal glow.")
    print("A magnificent pearl lies at the center of the cavern, radiating with light.")
    print("Do you attempt to retrieve the pearl?")

    response = ""
    while response not in yes_no:
      response = input("yes/no: ")
      print("\n")
      if response == "yes":
        print("You carefully approach the pearl, mindful of the dangers that may lurk in the depths.")
        retrieve_pearl()
      elif response == "no":
        print("You decide to leave the pearl undisturbed and return to the surface of the lake.")
        room_1()
      else:
        print("I didn't understand that. Try again\n")  

def monster_battle(monster_hp):

    global player_hp
    #Randomise the monster health points up to the maximum value
    monster_hp = dice_roll(monster_hp)

    while True:
        print("You have " + str(player_hp) + " health points remaining.")
        print("The monster has " + str(monster_hp) + " health points remaining.\n")

        print("You swing your sword at the monster")
        player_attack = dice_roll(6)

        if player_attack == 6:
            print("That was a powerful blow!")
            monster_hp -= 10
        else:
            print("You attack the monster and deal " + str(player_attack) + " damage.\n")
            monster_hp -= player_attack

        if monster_hp <= 0:
            print("You have defeated the monster with your final blow!\n")
            return
         
        print("The monster attacks you!")
        monster_attack = dice_roll(6)

        if monster_attack == 6:
            print("The monster has really hurt you!")
            player_hp -= 10
        else:
            print("The monster attacks you and deals " + str(monster_attack) + " damage.\n")
            player_hp -= monster_attack

        if player_hp <= 0:
            print("The monster strikes you down and you succumb to its deadly attack.")
            print("Game over.")
            quit()
    
              
def retrieve_pearl():
    print("As you reach for the pearl, a guardian of the cavern emerges, its eyes glowing with an eerie light.")
    print("The guardian challenges you to a battle to prove your worthiness to claim the pearl.")
    print("Do you accept the guardian's challenge?")

    response = ""
    while response not in yes_no:
      response = input("yes/no: ")
      print("\n")
      if response == "yes":
        print("You prepare to face the guardian in a battle of skill and determination.")
        monster_battle(20)
        final_area()
      elif response == "no":
        print("You turn and escape from the cavern, leaving the pearl behind.")
        room_1()
      else:
        print("I didn't understand that. Try again\n") 

def final_area():
   print("Congratulations, you have defeated the guardian of the cavern!")
   print("In doing so you have won the right to claim his majestic pearl!\n")

   print("You have won the game!")
   
intro()
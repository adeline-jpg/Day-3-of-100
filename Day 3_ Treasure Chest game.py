from token import LEFTSHIFT
#acii ART for this below
#' ' ' allows to have multiple lines of string"
print(r''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/__ ___"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction1 = input("Where should we go first? Left or Right\n").lower() #.lower() to take out case sensitivity
if direction1 == "Left".lower():
    print("You've reached the lake. There's an island in the middle of the lake.\n Would you like to swim or wait?")
    wait = input("Type \"wait\" to wait for boat. Type \"swim\" to swim across.\n").lower() #could use the slashes like that for incorporating the quotes, or you can also do ' '
    if wait == "wait".lower():
        print("you've reached the island and have come face to face with three doors, each with their own colors: Blue, Red, and Yellow.")
        door = input("Which door will you choose? Type \"Blue\", \"Red\", or \"Yellow\".\n").lower()
        if door == "Blue".lower():
            print("You've returned to the middle of the lake, this time without a boat. The Sirens will have you for dinner...RIP")
        elif door == "Red".lower():
            print("You've been burned by the Fire...RIP")
        elif door == "Yellow".lower():
            print("You Win! Here's a chest of gold and treasure map!")
            map = input("the map seems to be for this island. There is an \"x\" marked on the other side of an island. Do you want to go to it? \n Type \"yes\" or \"no\" \n").lower()
            if map == "yes".lower():
                dwarf = input("You bump into a dwarf on your way to the other side of the island. He asks for 4000 gold pieces, the same amount that you got from the treasure chest. \n Do you give it to him \n Type \"yes\" or \"no\"\n").lower()
                if dwarf == "yes".lower():
                    print("you're now broke, and he's kicked you off the island..womp womp. But hey, at least he got a boat for you!")
                else:
                    print("You don't give him your gold but the dwarf knows you are hiding some because he hears the gold clanging together as you walk. He pummels you until he's gotten all your goldleft. You are now broke and injured...RIP.")
            else:
                print("you took your gold back home! YAY!!")
        else:
            print("You tried to be creative, alas, you've unleashed the demons onto yourself...RIP...for now")
    else:
        print("a siren saw you swimming across and decided to have you as dinner...RIP")
else:
    print("You dropped down a well and is unable to get out...RIP")


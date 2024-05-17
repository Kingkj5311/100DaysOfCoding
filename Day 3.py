# Completed
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 
print("You fall from the sky, luckily you didn't die. You look up you see a sign that says 'Treasure Island'.")
print("You walk a bit and you see a fork in the road.")
direction=input("Do you want to go left or right? ").lower()
if direction=="left":
    print("You continue down the road to see a river.")
    action=input("Do you want to swim or wait for a boat? ").lower()
    if action == "wait":
        print("You wait for a boat to cross the river, it seems to be taking a while.")
        action=input("Do you want to swim or continue waiting for a boat? ").lower()
        if action == "swim" or action == "no":
            print("You attempt to swim across the river, but you can't swim.\n You Drown\nGAME OVER!!!")
        else:
            print("A boat arrives, they ask you how long you've been waiting.\nYou tell them it's been a while.\nThey offer you a free ride across the river.")
            action=input("Do you get on the boat? ").lower()
            if action == "yes":
                print("You get on the boat and they take you across the river.\nYou arrive at the island and see a cave.")
                action=input("Do you want to enter the cave? ").lower()
                if action == "yes":
                    print("You enter the cave and find three paths with colors on them.\nRed, Blue, Yellow.")
                    color=input("Which color do you choose? ").lower()
                    if color == "red":
                        print("You walk down the path and fall into a pitfall.\nGAME OVER!!!")
                    elif color == "blue":
                        print("You walk down the path and find a room with a treasure chest.\nYou open the chest and find a lot of gold.\nYOU WIN!!!")
                    elif color == "yellow":
                        print("You walk down the path and find a room with a dragon.\nYou get eaten by the dragon.\nGAME OVER!!!")
                else:
                    print("You choose not to enter the cave and go roaming around.\nYou see a house.")
                    action=input("Do you want to enter the house? ").lower()
                    if action=="yes":
                        print("You enter the house and find a witch.\nShe turns you into a frog.\nGAME OVER!!!")
                    else:
                        print("You lose interest in the island and head back to the crossroad\nYou choose to go right.")
                        print("You walk for a bit.\nOOPS!!! You fell into a pitfall and died.\nGoing out the way you came in.\nGAME OVER!!!")
            else:
                print("You refuse the boat ride and continue waiting.\nYou wait for a long time and die of starvation.\nGAME OVER!!!")
    elif action == "swim":
        print("You attempt to swim across the river, but you can't swim.\n You Drown\nGAME OVER!!!")
else:
    print("You walk for a bit.\nOOPS!!! You fell into a pitfall and died.\nGoing out the way you came in.\nGAME OVER!!!")

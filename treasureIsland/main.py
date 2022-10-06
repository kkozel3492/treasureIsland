# Treasure Island Choose Your Own Adventure
import sys

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

# Print out inital greeting and question
print("Welcome to Tresure Island.")
print("You and your crew will be searching for treasure on this mysterious island.")
print('You arrive on the island and see another group of bandits, do you fight'
      'or do you hide? Type "fight" or "hide"')

# Start while statement to decide outcome of first decision. If neither correct decision is made
# exit out of application, also exit if game over.

choiceOne = None
while choiceOne not in ("fight", "hide"):
    choiceOne = str(input("> "))

    if choiceOne == "hide":
        print("A tiger was hiding in the bushes and slaughtered your party")
        sys.exit("Game Over!")
        break
    if choiceOne == "fight":
        print("Your fearless crew fights off the bandits and cheers as the survivors run away!")
        break
    print("You have selected to neither fight or hide, a black hole opens aboves your crew"
          " and swallows everything in sight\n.....Including this game \n"
          "Let's try this again")

# Start Question 2
print("\n")
print("Your crew, exhausted after the thrilling fight, stop to rest over night. \n"
      "You know that someone must keep watch in case of an impending danger. \n"
      "Please choose either 'scruffy' or 'franklin' to watch over the camp at night.")

# Start Question 2 while loop, exit if wrong answer or game over.
choiceTwo = None
while choiceTwo not in ("scruffy", "franklin") and choiceOne != "hide":
    choiceTwo = input("> ")
    if choiceTwo == "scruffy":
        print("Scruffy found what he thought to be a bottle of rum on the beach. \n"
              "Scruffy, being the drunk that he is, decided it was safe to drink from this mystery bottle. \n"
              "It wasn't...... \n"
              "Scruffy died from the poison within the bottle, late at night, the same tiger hiding in the bushes \n"
              "early attacked your party, leaving most of your crew limbless and wounded on the beach. \n")
        sys.exit("Game Over!")
        break
    if choiceTwo == "franklin":
        print("Thankfully you didn't pick that drunk Scruffy. Franklin is always a safe bet. \n"
              "You're crew made it through the night")
        break
    print("You have selected to neither fight or hide, a black hole opens aboves your crew"
          " and swallows everything in sight\n.....Including this game \n"
          "Let's try this again")

print("\n")

# Start Question 3
print("You and your crew arrive to the cave that houses the treasure! \n"
      "upon entering you see three paths, two contain tigers, the other \n"
      "THE TREASURE \n"
      "Please choose path '1' '2' or '3'")

choiceThree = None

while choiceThree not in ('1', '2', '3'):
    choiceThree = input("> ")

    if choiceThree == '1':
        print("You make it to the end of the tunnel, and what do you see \n"
              "........... \n"
              "A TIGER!"
              )
        sys.exit("Game Over!")
        break

    if choiceThree == '2':
        print(".............Why are there so many tigers on this ISLAND!!! \n"
              "You are heard screaming as you are all being mauled by a tiger. \n"
              )
        sys.exit("Game Over!")
        break
    if choiceThree == '3':
        print("YOU DID IT! \n"
              "You and you're crew have survived Treasure Island, \n"
              "most of the other adventures have been murdered by tigers or bandits! \n"
              "\n"
              "\n"
              "\n"
              "CONGRATULATIONS!!!!!")
    print("You have selected to neither fight or hide, a black hole opens aboves your crew"
          " and swallows everything in sight\n.....Including this game \n"
          "Let's try this again")

input("press any key to exit")

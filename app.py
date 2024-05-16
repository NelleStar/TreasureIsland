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
print("Your mission is to find the treasure.") 

choice1 = input("You find yourself outside of an abandoned castle. Brushing away the cobwebs from the door you see that the lock is rusted over. You notice a window with broken glass to the side that you think you can jump through... Do you try to pick the lock or climb through the window? Type 'lock' or 'climb'. \n").lower()

if choice1 != 'lock' :
  print("You cut yourself on glass and fall on your face. Game over!")

choice2 = input("The lock pops open and the door swings inward with no resistance. As you walk into the dark hall you see that you can go right towards a room or straight down the hallway. You peek into room and see white curtains over all the furnature. The hallway only gets darker the further down  it goes. Where would you like to go? Type 'hall' or 'room'. \n").lower()

if choice2 != 'hall' :
  print("The floor gives out as you walk into the middle of the room and you land in a dungeon. Game over!")

choice3 = input("The further down the hall the more it slopes downward. Soon the air feels cooler and takes on the distinct smell of a space that hasn't been inhabited by humans for quite some time. Your hand, which was running along the wall to help guide you, feels slick with mildew. As you continue to stumble forward you reach an opening smaller than a doorway but larg enough to go through. Peeking through there is light on the other side. What do you do? Type 'crawl in' or ' 'turn around'. \n").lower()

if choice3 != 'crawl in' :
  print("As you turn to head back up the hall, something grabs your ankle and drags you back. Game over!")

choice4 = input("Straighting up, you realize that the room is expansive and there are torches on the walls that throw flickering, warm light against the hoard of treasures that lay before you. Atop a mound lays what looks to be a very old, very tired mouse. As you appraoch it sits up, blinks and says, 'Hello wanderer, welcome to the cave of chance. You may take one item but be wary for most things in here are not what they appear. Does anything catch your eye?' As you look around you see a few things that you think might be worth your time: a large red gem, a crown of gold, or a blue rug. Which do you choose? Type 'red', 'gold' or 'blue \n").lower()

if choice4 != 'blue':
  print("The mouse looks over as you reach for your item however it turns to dust in your hand. As you look down at the ash you hear 'Most treasure is an illusion but luckily you get to leave with your life.' As you walk out of the hall and back into the world you wonder if all are so lucky. Game over!")

if choice4 == 'blue':
  print("As you reach toward the blue rug it almost comes alive and unrolls itself. As you step forward to inspect it, it flies into the air, scoops you up and rolls itself tightly around you. As it nestles back into its spot you hear the mouse say 'Sometimes the leas likely items need to be fed.' It is in this moment you know you will neve leave alive. You lose!")
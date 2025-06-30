
print("==================== \n"
      " ROCK PAPER SCISSOR \n"
      "==================== \n \n")
print("1) ✊")  
print("2) ✋") 
print("3) ✌️ \n") 
rock = "✊" 
paper = "✋" 
scissor = "✌️" 

#player input
player = int(input("Pick a number:  "))
if player == 1:
    print("You chose: " + rock)
elif player == 2:
    print("You chose: " + paper)
elif player == 3:
    print("You chose: " + scissor)
else:
    print("Invalid input! Please chose between 1, 2 and 3")
  
#computer input
import random
computer = random.randint(1, 3)
if computer == 1:
    print("CPU chose: " + rock)
elif computer == 2:
    print("CPU chose: " + paper)
elif computer == 3:
    print("CPU chose: " + scissor)
else:
    print("Computer chose: " + "Error")

#for determining the player
if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
    print("YOU WIN!")
elif player == computer:
    print("IT IS A TIE")
else:
    print("YOU LOSE.")

import random

Choice = 0

#loop for system
while (True):
  System_choice = random.randint(1, 3)
  A_val = ""
  if System_choice == 1:
    A_val = "rock"
  elif System_choice == 2:
    A_val = "raper"
  elif System_choice == 3:
    A_val = "scissor"
  #print("System_choice is :", A_val)

#P_choice
  P_choice = input("Enter your Choice: ")
  P_choice = P_choice.lower()
  if P_choice == A_val:
    print("Game is Tie as System choice is:", A_val, "Player choose: ",P_choice)
  elif P_choice == "rock" and A_val == "paper":
    print("You loose as System choose:", A_val, "Player choose:", P_choice)
  elif P_choice == "paper" and A_val == "rock":
    print("You Win as System choose:", A_val, "Player choose:", P_choice)
  elif P_choice == "rock" and A_val == "scissor":
    print("You win as Sytem choose:", A_val, "Player choose:", P_choice)
  elif P_choice == "scissor" and A_val == "rock":
    print("You loose as System choose:", A_val, "Player choose:", P_choice)
  elif P_choice == "paper" and A_val == "scissor":
    print("You loose as System choose:", A_val, "Player choose:", P_choice)
  elif P_choice == "scissor" and A_val == "paper":
    print("You Win as System choose:", A_val, "Player choose:", P_choice)
  else:
    print("You enter Wrong Choice, please Enter rock, paper or scissor")
    continue
  user_input = input("Do you want to play more ? y/n")
  if user_input == 'y':
    continue
  else:
    print("Bye Bye!")
    break

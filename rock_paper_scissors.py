import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the game!\n")
game = [rock, paper, scissors]

player = int(input("Choose:\n0 = rock\n1 = paper\n2 = scissors\n"))

computer = random.randrange(0, 3)
if player != 0:
    print("You can choose only numbers 0, 1 and 2.")
elif player != 1:
    print("You can choose only numbers 0, 1 and 2.")
elif player != 2:
    print("You can choose only numbers 0, 1 and 2.")
print("Your choice:\n", game[player])
print("Computer's choice:\n", game[computer])

if player == 0 and computer == 2:
    print("You win!")
elif player == 1 and computer == 0:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 0 and computer == 1:
    print("You loose :(")
elif player == 1 and computer == 2:
    print("You loose :(")
elif player == 2 and computer == 0:
    print("You loose :(")
elif player == computer:
    print("Draw, try again!")

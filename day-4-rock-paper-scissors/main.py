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

shapes = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if (player_choice < 0) or (player_choice >= 3):
    print("You typed an invalid entry. You lose")
else:
    print("You chose:")
    print(shapes[player_choice])

    pc_choice = random.randint(0, len(shapes) - 1)
    print("Computer chose:")
    print(shapes[pc_choice])

    if (player_choice == 0) and (pc_choice == 2):
        print("You win")
    elif (pc_choice == 0) and (player_choice == 2):
        print("You lose")
    elif pc_choice > player_choice:
        print("You lose")
    elif player_choice > pc_choice:
        print("You win")
    else:
        print("Draw")

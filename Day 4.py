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
import random
List = [rock, paper, scissors]
Computer_Choice = random.choice(List)
Your_Choice = str(input('''Let's play a rock, paper and scissors game! What do you choose?
      Rock, Paper or Scissors? ''')).strip().capitalize()
if Your_Choice == "Rock":
    print(f" Your Choice = {rock}")
    print(f"Computer's Choice = {Computer_Choice}")
if Your_Choice == "Paper":
    print(f" Your Choice = {paper}")
    print(f"Computer's Choice = {Computer_Choice}")
if Your_Choice == "Scissors":
    print(f" Your Choice = {scissors}")
    print(f"Computer's Choice = {Computer_Choice}")

if Computer_Choice == Your_Choice:
    print("It's a draw")
elif Computer_Choice == rock:
    if Your_Choice == "Paper":
        print("You Win!")
    else:
        print("Computer Wins")
elif Computer_Choice == paper:
    if Your_Choice == "Scissors":
        print("You Win!")
    else:
        print("Computer Wins")
elif Computer_Choice == scissors:
    if Your_Choice == "Rock":
        print("You Win!")
    else:
        print("Computer Wins")
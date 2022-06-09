#!/usr/bin/python3
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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(user_choice)
computer_choice = random.randint(0,2)
print(computer_choice)

if user_choice == computer_choice:
    print("DRAW")
elif user_choice == 0 and computer_choice == 1:
    print(rock)
    print(paper)
    print("Paper wins.")
elif user_choice == 0 and computer_choice == 2:
    print(rock)
    print(scissors)
    print("Rock wins.")
elif user_choice == 1 and computer_choice == 0:
    print(paper)
    print(rock)
    print("Paper wins.")
elif user_choice == 1 and computer_choice == 2:
    print(paper)
    print(scissors)
    print("Scissors wins.")
elif user_choice == 2 and computer_choice == 0:
    print(scissors)
    print(rock)
    print("Rock wins.")
elif user_choice == 2 and computer_choice == 1:
    print(scissors)
    print(paper)
    print("Scissors wins.")

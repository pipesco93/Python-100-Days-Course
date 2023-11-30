import random 

# Print options

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


# Ask for rock paper or scissors
person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. " ))

print("You chose: ")
print(person_choice)
if person_choice == 0:
    print(rock)
elif person_choice == 1:
    print(paper)
elif person_choice == 2:
    print(scissors)

# Make computer choice
comp_choice = random.randint(0,2)

print("Computer chose: ")
print(comp_choice)

if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

if person_choice >= 3 and comp_choice < 0:
    print("You typed an invalid number, you lose!")
elif person_choice == 0 and comp_choice == 2:
      print("You win")
elif comp_choice > person_choice:
    print("You lose")
elif person_choice > comp_choice:
    print("You win!")
elif comp_choice == person_choice:
    print("It's a draw")
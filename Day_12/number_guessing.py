from random import randint
from art import logo

def check_answer(user_guess, number_to_guess):
    if user_guess > number_to_guess:
        return "+"
    elif user_guess < number_to_guess:
        return "-"
    else:
        return  "="




print(logo)

numbers =  randint(1, 100)



game_over = False




while not game_over:

    print("Welcome to number guessing game")
    
    print("I'm thinkig of a number between 1 and 100")

    level = input("Chose a level: 'easy' or 'hard': ")

    if level == "easy":
        attemps = 10
        print(f"You have {attemps} attemps")
    elif level == "hard":
        attemps = 5
        print(f"You have {attemps} attemps")

    number_to_guess = random.choice(numbers)
    while attemps > 0:
        guess = int(input("Make a guess: "))
        validation = check_answer(guess, number_to_guess)

        if validation == "+":
            print("too high")
            attemps -= 1
            print(f"you have {attemps} left")
        elif validation == "-":
            print("too low")
            attemps -= 1
            print(f"you have {attemps} left")
        elif validation == "=":
            print("Good guess")
            break

        if attemps == 0 andd:
            print("you lose")
      
    
    if input("Do you want to play again? 'y' or 'n': ") == "n":
        game_over = True


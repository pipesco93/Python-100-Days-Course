#Step 1  Imports
import random
from hangman_word_list import word_list
# List Stages of the game 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)-1

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

rand_word_index = random.randint(0 , len(word_list) - 1)
random_word =  random.choice(word_list)
word_len = len(random_word)


# Create a list with blancks to represent the word
display = []
for _ in range(word_len): #I ca unse underscore becaise i am not using the variable
    display.append("_")


#TODO-3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

end_of_game = False

print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

while not end_of_game:
    letter_guess = input("Guess a letter: ")


#TODO-4 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    
    for i in range(word_len):
        letter = random_word[i]
        if letter == letter_guess:
            display[i] = letter

#If lives goes down to 0 then the game should stop and it should print "You lose."
    if letter_guess not in random_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was {random_word}")
#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    

#Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
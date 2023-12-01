#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open ("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open ("./Input/Letters/starting_letter.txt") as start_letter:
    content = start_letter.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="a") as complete:
            complete.write(new_letter)



# this method works but with som elimitation id you keep adding the same content under the previous letter
# for name in name_list:
#     clean_name = name.strip()
#     first_line = lines[0].replace("[name]",clean_name)
#     lines[0] = first_line
#     with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="a") as new_letter:
#         for line in lines:
#             new_letter.write(line)





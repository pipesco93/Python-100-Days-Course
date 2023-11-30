alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def cesar(plain_text , shift_amount, direction):

    #TODO: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. plain_text = "hello", shift = 5, cipher_text = "mjqqt", print output: "The encoded text is mjqqt"
    message = ""
    for i in plain_text:

        if i in alphabet:
            if direction == "encode":
                new_index = alphabet.index(i) + shift_amount
                print(new_index)
                if new_index > len(alphabet) - 1:
                    new_index = (new_index - len(alphabet))
                    print(new_index)
                message += alphabet[new_index]
    
            
            if direction == "decode":
                new_index = alphabet.index(i) - shift_amount
                message += alphabet[new_index]
        else:
            message += i


    if direction == "encode":
        print(f"The encoded text is {message}")
    elif direction == "decode":
        print(f"The docoded text is {message}")        
    


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
should_continue =  True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesar(text , shift, direction )
    result = input("Type 'yes'if you want to continue otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Good by")
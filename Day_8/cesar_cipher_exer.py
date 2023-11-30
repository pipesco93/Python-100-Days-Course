from operator import index


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text , shift_amount):

    #TODO: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. plain_text = "hello", shift = 5, cipher_text = "mjqqt", print output: "The encoded text is mjqqt"
    encode_message = ""
    for i in plain_text:
        new_index = alphabet.index(i) + shift_amount

        if new_index > len(alphabet) - 1:
            new_index = shift_amount - 1
        encode_message += alphabet[new_index]
    #encode_message = "".join(encode_message)
    print(f"The encoded text is {encode_message}")
    return encode_message


#TODO: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.        

def decrypt(encoded_msg , shift_amount ):
    decoded_message = ""
    for i in encoded_msg:
        new_index = alphabet.index(i) - shift_amount
        decoded_message += alphabet[new_index]
    print(f"The docoded text is {decoded_message}")



#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


if direction == "encode":
    encrypt(text , shift)
elif direction == "decode":
    decrypt(text, shift)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
            shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char    
    print(f"The {direction}d text is {cipher_text}")

should_continue = True
while should_continue:
#input parameters.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
# reduce shift .
    shift = shift % 25
    caesar(text, shift, direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == 'no':
        should_continue = False
        print("GoodBye!")
# TODO-2 : Create a function called 'decrypt' that the 'text' and 'shift' as inputs.
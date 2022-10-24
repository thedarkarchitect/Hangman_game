from pickle import FALSE
from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)



def Casear(text, shift_amount, cipher_direction):
    global alphabet
    final_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for i in text:

        if i in alphabet: 
            position = alphabet.index(i)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += i
        

    print(f"Here's the  {cipher_direction} result : {final_text}\n")



is_true = True
while is_true:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 27 
    Casear(text, shift, direction)
    

    if input("Enter 'yes' to continue and 'no' to stop ") == "no":
        is_true  = False
        print("Goodbye")
        
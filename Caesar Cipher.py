import os
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',  'z']

print(logo)

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift % 26
    
    
    def encrypt(plain_text, shift_amount):
        cipher_text=""
        for char in plain_text:
            if char in alphabet:
                position= alphabet.index(char)
                new_position= position + shift_amount
                cipher_text += alphabet[new_position]
            else: cipher_text += char

        print(f"The encoded text is {cipher_text}")    

                    
    def decrypt(cipher_text, shift_amount):
        plain_text=""
        for char in cipher_text:
            if char in alphabet:
                position= alphabet.index(char)
                new_position= position - shift_amount
                plain_text += alphabet[new_position]
            else: plain_text+= char    
        print(f"The decoded text is {plain_text}")

    if direction== "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction== "decode":
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("You entered a wrong option")   

    result=input("Type 'YES' if you want to go again. Otherwise type 'NO'.\n").lower()
    if result=="no":
        should_continue=False
        print("Goodbye!")
    os.system('cls' if os.name=='nt' else 'clear')    
    



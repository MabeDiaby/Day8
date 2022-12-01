from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     decoded_text = ""
#     if direction == "encode":
#         for letter in plain_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             new_letter = alphabet[new_position]
#             decoded_text += new_letter
#         print(f"The encoded text is {decoded_text}")
#     else:
#         print("Invalid directions try again")
# def decrypt(cypher_text, shift_amount):
#     encoded_text = ""
#     if direction == "decode":
#         for letter in cypher_text:
#             position = alphabet.index(letter)
#             prev_position = position - shift_amount
#             prev_letter = alphabet[prev_position]
#             encoded_text += prev_letter
#         print(f"Your decoded text is {encoded_text}")

# REFACTOR
    
print(logo)
should_continue = True

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_posiiton = position + shift_amount
            end_text += alphabet[new_posiiton]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    continued = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    if continued == "no":
        should_continue = False
        print("Goodbye")
    
    # decoded_arr.append(list(text))
    # print(decoded_arr)
# encrypt(plain_text = text, shift_amount = shift)
# decrypt(cypher_text = text, shift_amount = shift)
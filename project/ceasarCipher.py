alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
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

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        new_posiiton = position + shift_amount
        end_text += alphabet[new_posiiton]
    print(f"The {cipher_direction}d text is {end_text}")
    

caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    # decoded_arr.append(list(text))
    # print(decoded_arr)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# encrypt(plain_text = text, shift_amount = shift)
# decrypt(cypher_text = text, shift_amount = shift)
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# Step 2
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# Step 3
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# Caesar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


# Create a function called 'encrypt' that takes the text and shift as inputs
# Inside the 'encrypt' function, shift each letter of the text forwards in the alphabet by the shift amount and print the encripted text
# Check if user wanted to encrypt or decrypt the message. 


def encrypt(text, shift):

    encrypted_word = ""

    for i in text:
    
        letter_index = alphabet.index(i)
        encrypted_word += alphabet[letter_index + shift]

    print(f"The encrypted word is {encrypted_word}.")


def decrypt(text, shift):

    decrypted_word = ""

    for i in text:
        letter_index = alphabet.index(i)
        decrypted_word += alphabet[letter_index - shift]

    print(f"The decrypted word is {decrypted_word}.")


task = input("Do you want to encode or decode?\n")

if task == "encode":
    text_to_encode = input("Text to encode: ")

    encrypt(text_to_encode, 1)

elif task == "decode":
    text_to_decode = input("Text to decode: ")
    
    decrypt(text_to_decode, 1)






 

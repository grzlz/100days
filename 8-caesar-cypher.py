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


keep_working = True

while keep_working:
    
    task = input("Do you want to encode or decode?\n")
    text = input("Write your message: ")
    shift = int(input("Type the shift number: "))

    if task == "encode":
        encrypt(text, shift)

    elif task == "decode":
        decrypt(text, shift)

    if input("Do you want to continue? ") == "No":
        keep_working = False






 

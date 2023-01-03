# Caesar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


# Create a function called 'encrypt' that takes the text and shift as inputs
# Inside the 'encrypt' function, shift each letter of the text forwards in the alphabet by the shift amount and print the encripted text

def encrypt(text, shift):
    
    encrypted_word = ""

    for i in text:
    
        letter_index = alphabet.index(i)
        encrypted_word += alphabet[letter_index + shift]

    print(f"The encoded word is {encrypted_word}")

encrypt("zulu", 1)
 

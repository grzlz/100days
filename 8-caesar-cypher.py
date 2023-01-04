# Caesar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


# Create a function called 'encrypt' that takes the text and shift as inputs
# Inside the 'encrypt' function, shift each letter of the text forwards in the alphabet by the shift amount and print the encripted text
# Check if user wanted to encrypt or decrypt the message. 
# Combine both functions into a function calles caesar with three arguments: text, shift and task


def caesar(text, shift, task):
    if task == "decode":
        shift *= -1

    new_word = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        new_word += alphabet[letter_index + shift]
    
    print(f"You requested to {task} and the word is: {new_word}")

keep_working = True

while keep_working:
    
    task = input("Do you want to encode or decode?\n")
    text = input("Write your message: ")
    shift = int(input("Type the shift number: "))

    caesar(text, shift, task)

    if input("Do you want to continue? ") == "No":
        keep_working = False



    


 

# Caesar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Create a function called 'encrypt' that takes the text and shift as inputs
# Inside the 'encrypt' function, shift each letter of the text forwards in the alphabet by the shift amount and print the encripted text

def encrypt(text, shift):
    
    text_list = [i for i in text]

    encrypted_word = []

    for i in range(len(text_list)):
        print(i)

        for j in range(len(alphabet)):
            print(j)

            if alphabet[j] == text_list[i]:

                print(alphabet[j], text_list[i], alphabet[j + shift])
                encrypted_word += alphabet[j + shift]

    print("".join(encrypted_word))

encrypt("funciona", 2)


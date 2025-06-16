#stores the code of encrypting and decrypting basics

import string

#it uses all the letters, digits, punctuation and space from the imported string module
letters= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
#print(letters) just testing to see what the letters variable contains
letters= list(letters) #converting it to list so that it is iterable in the for loop

#functions for encrypting and decrypting the message using caeser cipher
def encrypt(message,shift):  # function for encrypting the message
    encrypt_mess=""  #initializing an empty string to store the encrypted message
    for charr in message:
        if charr in letters:
            index=letters.index(charr) #finding the index of the character in the message from the letters list
            new_index=(index + shift) % len(letters)  #caeser cipher = (text + shift) % 26, we take 26 as it is the length of the alphabet set but here expanded hece the length of the letters taken
            encrypt_mess += letters[new_index] #adding the new encrypted charcter 
        else:
            encrypt_mess += charr #adding the character as it is if it is not in the letters list
    print("THE ENCRYPTED MESSAGE IS: ", encrypt_mess)

def decrypt(message,shift):
    decrypt_mess="" # intializing for storing the decrypted message string
    for charr in message:
        if charr in letters:
            index=letters.index(charr)
            new_index = (index-shift ) % len(letters) 
            decrypt_mess += letters[new_index]
        else:
            decrypt_mess += charr 
    print(" THE DECRYPTED MESSAGE IS : ", decrypt_mess)

#the main program to call the fucntions and take user inputs to display the encryted and the decrypted message
print("======THE CAESER PROGRAM=========")
print("This program will encrypt and decrypt a message using the caeser cipher")
input_ed= input("Do you want to encrypt or decrypt the message? (e/d):").lower() #it asks the user if they want  to encrypt pr decrypt the messgae and converts whaterever they typed to lower as we expect it to lower for the if condition
if input_ed not in ["e", "d"]: #if the user does not type e or d, it will print an error message and exit
    print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")
elif input_ed == "e":
    message = input("enter the message you want to encrypt: ")
    shift = int(input("enter the shift value (1-25): "))
    encrypt(message,shift)
elif input_ed == "d":
    message=input("enter the message  to be decrypted: ")
    shift= int(input("enter the shift value (1-25): "))
    decrypt(message,shift)
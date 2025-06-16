#stores the code of encrypting and decrypting basics

import string

#it uses all the letters, digits, punctuation and space from the imported string module
letters= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
#print(letters) just testing to see what the letters variable contains
letters= list(letters) #converting it to list so that it is iterable in the for loop





print("======THE CAESER PROGRAM=========")
print("This program will encrypt and decrypt a message using the caeser cipher")



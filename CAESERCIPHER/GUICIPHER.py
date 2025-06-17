import string #for all the letters, digits, punctuation and space 
import tkinter as tk #for the GUI
from tkinter import messagebox #for displaying messages out and error messages

text = list(string.ascii_lowercase + string.ascii_uppercase +string.digits + string.punctuation + " " )
def encrypt(message,shift):
    encrypt_mess = "" #initalizing an empty string to store the encrypted message
    for charr in message: #for all the characters in the message
        if charr in text: #of a character is in the text list
            index=text.index(charr) #assigning the index of the character in message from the text list
            new_index= (index + shift) % len(text) #caeser cipher = (text + shift) % 26, we take 26 as it is the length of the alphabet set but here expanded hence the length of the text taken
            encrypt_mess += text[new_index] #adding the new encrypted character to the encrypted message 
        else:
            encrypt_mess += charr #if the character not in the text list then it returns the cahracter as it is
    return encrypt_mess #returning the encrypted message

def decrypt(message, shift):
    decrypt_mess=""
    for charr in message:
        if charr in text:
            index=text.index(charr)
            new_index= (index - shift) % len(text)
            decrypt_mess +=text[new_index]
        else:
            decryot_mess +=charr
    return decrypt_mess 

def process_cipher():
    mode = mode_var.get() # select mode encrypt or decrypt in radio buttons
    message = message_entry.get("1.0", tk.END).strip() #to get the text from the message box to encrypt or decrypt
    shift_str = shift_entry.get() #ot get shift value from the textbox for the shift in caeser cipher algorithm
    
    #validating the inputs
    if not message:
        messagebox.showerror("ERROR", "Kindly enter a message, don't leave it empty.")
        return #this condition checks if the message box is empty or not and if empty asks the users to fill a message
    
    if not shift_str.isdigit():
        messagebox.showerror("ERROR","Kindly enter a valid interger between 1 and 25 for the shift value.")
        return #this condition checks if the shift value is a number and not other alphabet or alphanumberic 
    
    shift = int(shift_str) #if a valid digit then it converts the shift_str to integer
    
    if shift <1 or shift > 25:
        messagebox.showerror("ERROR", "Kindly enter the shift value between 1 and 25.")
        return #this condition checks if the shifit entered is in the range of 1 to 25 or not
    
    #if all the inputs are validagted to fall in the correct range of shift and a message is entered then the following code
    
    if mode == "ENCRYPT": #according to the mode choosen the function is called
        result =encrypt(message,shift)
    else:
        result = decrypt(message, shift)
    
    #making the result message box to display the readonly message outputed after encryption or decryption
    result_text.config(state='normal')  #this keeps the text widget editable for the programmer and not for the user
    result_text.delete("1.0",tk.END) #this deletes the prior whole text froms tart to end with its trailing newine as well 
    result_text.insert(tk.END,result) #this inserts the new everytime encrypted or decrypted message at the end of the prior text 
    result_text.config(state='disabled') #this keeps the result the output message only readable for the user and can't edit the output result message box
    

#creating the gui for the caeser cipher pragram
window= tk.Tk() #this creates the main window object in tkinter, parent widget which holds the other widgets
window.title("CAESER CIPHER") #this sets the title top bar of the window 
window.geometry("800x600") #sets the size of the window in pixels
window.resizable(False,False) #this disables the resizing of the window

#label title for the page
tk.Label(window, text="THE CAESER CIPHER PROGRAM", font=('Times New Roman', 18,'bold italic')).pack(pady=8)

#creating the radio buttons for the mode selection
mode_var = tk.StringVar(value='ENCRYPT') #StringVar holds the selected mode either encrypt or decrypt and default is encrypt as first encrypt to decrypt
tk.Label(window, text='Select Mode:', font=('Times New Roman', 14,'bold')).pack(anchor=tk.W,padx=20) #creates a label with text in courier font and size 14 and bold, saying select mode
tk.Radiobutton(window, text='ENCRYPT', variable= mode_var, value='ENCRYPT',font=('Times New Roman', 11,'bold')).pack(anchor=tk.W, padx=20) #creates a radio button for encrypt and positioned in west and padding horizontally 20 pixels
tk.Radiobutton(window,  text='DECRYPT', variable =mode_var, value = 'DECRYPT',font=('Times New Roman', 11,'bold')).pack(anchor=tk.W,padx=20) #does the same for the decrypt radio button

#taking message input from the user
tk.Label(window, text='Enter Message: ',font=('Times New Roman', 14, 'bold' )).pack(anchor=tk.W,padx=20) #this creates a label to enter message
message_entry= tk.Text(window, height=6, width=54, font=('Times New Roman', 12))
message_entry.pack(anchor=tk.W,padx=20) #this creates a text box to enter the message with height 6 and width 54 and font size 12

#taking shift value input from the user
tk.Label(window, text='Enter the shift value(1-25): ', font=('Times New Roman', 14, 'bold')).pack(anchor=tk.W,padx=20) #this creates the label to enter the shift value
shift_entry = tk.Entry(window,font=('Times New Roman', 12))#this creates an entry box to enter the shift value with font size 12
shift_entry.pack(anchor=tk.W,padx=20) 

#creating the button which call the function process_cipher
tk.Button(window, text='CIPHER', command=process_cipher,font=('Times New Roman',14)).pack(pady=10)

#result display box
tk.Label(window, text='Result: ', font=('Times New Roman',14,'bold')).pack(anchor=tk.W,padx=20)
result_text =tk.Text(window,height=6,width = 54,state='disabled',font=('Times New Roman',12))
result_text.pack(anchor=tk.W,padx=20) #this creates a text box to display the result with height 6 and width 54 and font size 12, state is disabled so that the user can't edit the output message

window.mainloop()
    
    
    
  
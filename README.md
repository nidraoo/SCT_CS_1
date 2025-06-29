# SCT_CS_1
A modern Python application with a clean Graphical Interface (GUI) to encrypt and decrypt using the Caeser Cipher Algorithm.
Built with Tkinter, this tool is beginner-friendly, visually intuitive, and packed with helpful features.

## What is a Caeser Cipher?
The Caeser Cipher is a substitution cipher where each character in the plaintext is shifted a certain number of places the character set. 
This project goes beyond just the alphabet and supports the entire printable ASCII set, making it much more robust and versatile than the traditional version.

## Features
- Encrypt and decrypt text using the Caeser Cipher Logic
- Simple, clean, and user-friendly GUI built with Tkinter
- Mode of selection is done using radio buttons
- The encrypted/decrypted result to copied to clipboard
- One-Click Clear All functionality
- Validations for the input messages and shift value and helpful error messages
- Read-Only result box to prevent accidental edits from the user

## How It Works

1. **Select Mode:** Choose between **Encrypt** or **Decrypt** using radio buttons.
2. **Enter Message:** Type your message in the text box (supports letters, digits, and symbols).
3. **Set Shift Value:** Enter a number between **1 and 25** as the Caesar Cipher shift.
4. **Convert:**
   - Click the **Convert** button to encrypt or decrypt the message.
   - Output is shown in a read-only box below.
5. **Extra Features:**
   -  **Copy Result**: Copies the output to clipboard.
   -  **Clear All**: Clears all input and output fields for a fresh start.

### Prerequisites 
- Python 3.x
- Tkinter (Module of Python)

### Installation
```bash
git clone https://github.com/nidraoo/SCT_CS_1.git               
cd CAESERCIPHER   
py GUICIPHER.py


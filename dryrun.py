# This is a script that I created so that it can print a list of files to be encrypted or decrypted without actually performing the encryption or decryption

import os
from cryptography.fernet import Fernet
import argparse

# Function to encrypt a single file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_encrypted)

# Function to decrypt a single file
def decrypt_file(file_path, secret_key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_decrypted)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Encrypt or decrypt files in a directory.")
parser.add_argument("--decrypt", action="store_true", help="Decrypt files")
parser.add_argument("--dry-run", action="store_true", help="Perform a dry run (list files without encrypting/decrypting)")
args = parser.parse_args()

# List of files to exclude from encryption/decryption
exclude_files = ["encrypt.py", "thekey.key", "decrypt.py"]

# Load the secret key
with open("thekey.key", "rb") as key:
    secret_key = key.read()

# Determine whether to encrypt or decrypt
if args.decrypt:
    process_function = decrypt_file
    action = "Decryption"
else:
    process_function = encrypt_file
    action = "Encryption"

# Dry run: List files without actually processing them
if args.dry_run:
    print(f"Dry Run - {action} Preview:")
else:
    print(f"Starting {action}...")

# Traverse all subdirectories and process files in each directory
for root, dirs, files in os.walk('.'):
    for file in files:
        # Skip files that should not be processed
        if file in exclude_files:
            continue

        # Get the full path of the file
        file_path = os.path.join(root, file)

        # Dry run: Print the file path without processing it
        if args.dry_run:
            print(file_path)
        else:
            # Process the file (encrypt or decrypt)
            process_function(file_path, secret_key)

if not args.dry_run:
    print(f"{action} completed.")

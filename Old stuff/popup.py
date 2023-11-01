import tkinter as tk 
from tkinter import messagebox
from tkinter import simpledialog


root = tk.Tk()
root.withdraw()  # Hide the main window


messagebox.showinfo("Encryption Complete", "You have been hacked. Toss a Bitcoin here at *********** to receive your files back ;) ")

messagebox.showinfo("message", "Bitcoin received, secret code is 'coffee'. Now running decryption. Click ok to continue.")


while True:
    user_input = simpledialog.askstring("Input", "Enter the secret phrase to decrypt your files:")
    if user_input != "coffee":
        messagebox.showinfo("message", "Try again fool!")
    else:
        messagebox.showinfo("message", "Thanks loser :) You can have your files back now")
        break  # Exit the loop when the correct phrase is entered


# Keep the window open until the user closes it
root.mainloop()
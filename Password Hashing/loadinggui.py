import os # Importing os library to interact with the operating system
import tkinter as tk # Importing tkinter for gui
from tkinter import simpledialog # Importing simpledialog for user input
from tkinter import messagebox # Importing messagebox for user yes and no input

def load_gui():
    # Opens up tkinter (GUI)
    root = tk.Tk()
    root.withdraw()
    root.title("LOGIN")
    
    # Opens up the GUI for asking the user if they have an account with us (Whether or not they should register or login)
    response = messagebox.askyesno("Register/Login", "Do you have an account with us?")

    # Below code is just for GUI purposes, actual functionality is within main
    if not response: # User inputted NO
        username = simpledialog.askstring("Username registration", "Enter a username: ")
        plain_password = simpledialog.askstring("Password registration", "Enter a password: ")
        return username, plain_password, response
    else: # User inputted YES
        username = simpledialog.askstring("Username", "Enter your username: ")
        plain_password = simpledialog.askstring("Password", "Enter your password: ")
        return username, plain_password, response
        
    
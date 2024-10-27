# Importing functions from other classes
from loadinggui import load_gui
from User import register_user
from User import authenticate_user

def login():
    x = True
    
    # Login loop
    while x == True:
        # Calls "load_gui" function from loadinggui class and sets the certain variables with the returned variables
        username, plain_password, response = load_gui()
    
        if not response: # User inputted YES (They need to make a account)
            register_user(username, plain_password)
        else: # Use inputted NO (They already have an account, we need to authenticate)
            # If the "authenticate_user" function returns "True" then... (User inputted the correct username and password)
            if authenticate_user(username, plain_password):
                print("Login SUCCESSFULL")
                # Stop login loop
                x = False
            # If the "authenticate_user" function returns "False" then... (User inputted the incorrect username and password)
            else:
                print("LOGIN FAILURE")
                # NOTE: Login loop will continue UNTIL user inputs a correct username and password combination


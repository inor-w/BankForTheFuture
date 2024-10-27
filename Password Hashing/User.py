import bcrypt
import csv
import os

CSV_FILE = 'cred.csv'

def register_user(username, plain_password):
    # Generate a unique user ID and hash the password
    user_id = os.urandom(8).hex()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')

    # Write user data to CSV, ensuring headers are added only if missing
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['user_id', 'username', 'password_hash']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header if file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        # Write user data
        writer.writerow({
            'user_id': user_id,
            'username': username,
            'password_hash': hashed_password
        })
    
    print("SUCCESSFUL REGISTRATION")

def authenticate_user(username, plain_password):
    try:
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print("CSV Headers:", reader.fieldnames)  # Debugging line
            
            for row in reader:
                print("Row Data:", row)  # Debugging line
                if row['username'] == username:
                    stored_hash = row['password_hash']
                    if bcrypt.checkpw(plain_password.encode('utf-8'), stored_hash.encode('utf-8')):
                        #print("Login successful.")
                        return True
                    else:
                        #print("Invalid username or password.")
                        return False
            print("Invalid username or password.")
            return False
    except FileNotFoundError:
        print("User data file not found.")
        return False

# User input and registration/authentication
#username = input("What is your username?: ")
##plain_password = input("What is your password?: ")
#register_user(username, plain_password)
#authenticate_user(username, plain_password)

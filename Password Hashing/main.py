# Importing functions from other classes
from login import login
import money

def main():
    login()
    money.enter()

# Calls main
if __name__ == "__main__":
    main()
import random
from user import User
from credentials import Credentials

def create_user(platform, username, password):
    new_user = User(platform, username, password)
    return new_user


def save_user(user):
    user.save_user()

def del_user(ind):
    Credentials.delete_user(ind)


def display_credentials():
    
    return Credentials.display_credentials()




def main():
    print("Welcome to Password Locker")
    print('\n')
    print("Select a short code to navigate through:To create a new user use 'nu' To login to your account 'lg' or 'ex' to exit")
    short_code = input().lower()
    print('\n')

    if short_code == "nu":
        print("Create a new account!")
        print("Create username")
        new_user = input()

        print("Create Password")
        new_password = input()

        print("Confirm Password")
        confirm_pass = input()

    elif short_code == "lg": 
        print("Enter your credentials to login")
        print("Enter your username")
        username = input()

        print("Enter your password")
        password = input()


    elif short_code == "ex":
        print("Thank you for using password locker login again soon, Goodbye!")
        print("\n")
        

        

if __name__ == '__main__':
                """main function to run the module"""
main()
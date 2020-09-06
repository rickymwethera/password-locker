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
    print("its working")

if __name__ == '__main__':
                """main function to run the module"""
main()
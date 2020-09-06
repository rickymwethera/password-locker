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
        username = input()

        print("Create Password")
        print("If you desire to type in your own password user the short code 'mine' and code 'g' for use to generate one for you")
        new_password = input()

        if new_password == "mine":
            print("okay, type in your password")
            password = input()
            if password == 'mine':
                print('\n')
                print('Kindly enter your prefered password: (Your password is safe with us)')
                password = input()
                print('\n')
                print('Password stored successfully')
                print("Account setup complete")

            elif passcode == 'g':
                    print('\n')
                    password = random.randint(34567,98756)
                    print('\n')
                    print("Password generation is SUCCESSFUL!")
                    print("Account setup complete")
            

        # else new_password =="g":


    # save_user(create_user(username,password))
    #     print()

    elif short_code == "lg": 
        print("Enter your credentials to login")
        print("Enter your username")
        username = input()

        print("Enter your password")
        password = input()


    elif short_code == "ex":
        print("Thank you for using password locker login again soon, Goodbye!")
        print("\n")

    else:
        print("Please use the short codes!")
        

        

if __name__ == '__main__':
                """main function to run the module"""
main()
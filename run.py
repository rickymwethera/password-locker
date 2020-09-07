import random
from user import User
from credentials import Credentials

def create_user(username, password):
    '''creates a new user and gets the blueprint from user class'''
    new_user = User(username, password)
    return new_user


def save_user(user):
    user.save_user()

def user_verification(username,password):
    '''
	Function that verifies the existance of the user before allowing login
	'''
    ifexists=''
    for user in User.user_list:
        if (user.username == username and user.password == password):
                    ifexists = user.username
        return ifexists

def del_user(ind):
    Credentials.delete_user(ind)


def display_credentials():
    
    return Credentials.display_credentials()

def new_creds(username,password):
    '''function creates new credentials'''
    created_creds = Credentials(username,password)
    return created_creds

def save_creds(credentials):
    '''this function saves the new credentials'''
    Credentials.save_creds(credentials)



#main function execution
def main():
    while True:
        print("Welcome to Password Locker")
        print('\n')
        print("Select a code to navigate through:To create a new user use 'nu' To login to your account 'lg' or 'ex' to exit")
        nav_code = input().lower()
        print('\n')

        if nav_code == "nu":
            print("Create a new account!")# creating a new user account
            print("Create username")
            username = input()

            print("Create Password")
            print("If you desire to type in your own password user the short code 'mine' and code 'g' for use to generate one for you")
            new_password = input()

            if new_password == 'mine':
                print('\n')
                print('Kindly enter your prefered password: (Your password is safe with us)')
                password = input()
                print('\n')
                print('Password stored successfully')
                print("Account setup complete")

            elif new_password == 'g':
                print('\n')
                password = random.randint(10000,98765)#randomly searches for a password from between the figures given
                print('\n')
                print(f"Your new password is {password}")
                print("Password generation is SUCCESSFUL!")
                print("Account setup complete")

            save_user(create_user(username,password))
            print("details have been saved!")
                

       

        elif nav_code == "lg": 
            print("Enter your credentials to login")
            print("Enter your username")
            username = input()

            print("Enter your password")
            password = input()

            status= user_verification(username,password)
            if status == username:

                while True:

                    print(f"Hello {username} Welcome, you are now logged in")

                    print("Here is a list of commands and their functions. 'add' - adds account 'disp' -displays account details' 'del-deletes account' 'out - logout' ")
                    nav_code = input().lower()

                    if nav_code == 'disp':
                        if display_credentials():
                            print("This is a list of all your stored usernames and passwords")

                            for credentials in display_credentials():
                                print(f"USERNAME: {credentials.username} \nPASSWORD: {credentials.password}\n")
                                print("*"*50)

                        else:
                            print("You do not have any saved details")

                    elif nav_code == 'add':
                        print("Great, add a new account below")
                        print("Enter your username")
                        username = input()
                        print("Create Password")
                        print("If you desire to type in your own password user the short code 'mine' and code 'g' for use to generate one for you")
                        new_password = input()

                        if new_password == 'mine':
                            print('\n')
                            print('Kindly enter your prefered password: (Your password is safe with us)')
                            password = input()
                            print('\n')
                            print('Password stored successfully')
                            print("Account setup complete")

                        elif new_password == 'g':
                            print('\n')
                            password = random.randint(10000,98765)
                            print('\n')
                            print(f"{password}")
                            print("Password generation is SUCCESSFUL!")
                            print("Account setup complete")
                        #now lets save the credentials created so that they can be viewed on disp
                        save_creds(new_creds(username,password))
                        print("new credentials have been saved")

                        
                    elif nav_code == "out":#logout from user account to home 
                        print("Thank you for using password locker login again soon, Goodbye!")
                        print("\n")
                    else:
                        print("Please use the codes available")
            else:
                print("*"*50)
                print("Wrong username or password, please try again")
                print("*"*50)




        elif nav_code == "ex":#exiting the program
            print("Thank you for using password locker login again soon, Goodbye!")
            print("\n")

        else:
            print("Please use the codes!")
        

        

if __name__ == '__main__':
                """main function to run the module"""
main()
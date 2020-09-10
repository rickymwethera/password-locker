from user import User

class Credentials:
    new_user_list = []

    def __init__(self, username, password):
        
        self.username = username 
        self.password = password

    def save_creds(self):
        Credentials.new_user_list.append(self)
    
        """function to display all available accounts"""
    
    def display_credentials():
        """
        method that returns the credential array
        """
        return Credentials.new_user_list

    def delete_account(credential):
        Credentials.new_user_list.remove(credential)
        return credential
    
    def find_account(username): # this is for verification of the user
        for credential in Credentials.new_user_list:
            if credential.username == username:
                
                return credential

    
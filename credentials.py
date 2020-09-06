from user import User

class Credentials:
    new_user_list = User.user_list

    def __init__(self, platform, username, password):
        self.platform = platform
        self.username = username 
        self.password = password

    def save_user(self):
        User.user_list.append(self)
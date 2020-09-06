class User:
    """new users creation"""
    user_list = []

    def __init__(self,username, password, platform):
        self.username = username
        self.password = password
        self.platform = platform
        


    def save_user(self):
        """add user into user_list"""
        User.user_list.append(self)
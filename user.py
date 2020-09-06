class User:
    """new users creation"""
    user_list = []

    def __init__(self,username, password):
        self.username = username
        self.password = password
        
        


    def save_user(self):
        """add user into user_list"""
        User.user_list.append(self)
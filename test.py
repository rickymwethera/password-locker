import unittest
from user import User 
from credentials import Credentials 

class TestUser(unittest.TestCase):
    """test case to test user methods"""
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ricky","123123") # create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.new_credentials = []    
         
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"ricky")
        self.assertEqual(self.new_user.password,"123123")
  
    def test_save_login(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)



class TestCredentials(unittest.TestCase):
    """test case to test credentials methods"""
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile = Credentials("ricky","123123") # create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.new_credentials = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_profile.username,"ricky")
        self.assertEqual(self.new_profile.password,"123123")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the user list
        '''
        self.new_profile.save_creds() # saving the new credentials
        self.assertEqual(len(Credentials.new_credentials),0)


    def test_delete_credentials(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_profile.save_creds()
            test_credential = Credentials("ricky","123123") # new contact
            test_credential.save_creds()

            self.new_profile.delete_account()# Deleting a contact 
            self.assertEqual(len(Credentials.new_user_list),1)

if __name__ == '__main__':
    unittest.main()
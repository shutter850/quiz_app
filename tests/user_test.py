import unittest
from modules.User import User

#unittest.TestCase child class for testing the user class
class UserUnitTest (unittest.TestCase):
    @classmethod
    def setUpClass (self):
        self.user = User('Abdullahi',30)
    def test_is_score_reduce_function_functional (self):
        self.user.reduceScore(2)
        self.assertEqual(self.user.getScore(), 28 , 'Score could not be reduced successfully!')
    def test_can_get_username(self):
        self.assertEqual(self.user.getUsername(),'Abdullahi', "Can't get username")    
         
        
        

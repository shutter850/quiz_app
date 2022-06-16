import unittest
from modules.Auth import Auth

#unittest.TestCase child class for testing the auth class
class AuthUnitTest (unittest.TestCase):
    @classmethod
    def setUpClass (self):
        self.auth = Auth()
    def test_compare_password_should_return_false (self):
        self.auth.password='123456'
        self.assertEqual(self.auth.comparePassword(), False , 'comparePassword method did not return false when wrong password is passed')
      
         
        
        

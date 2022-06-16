import os
from dotenv import load_dotenv
from colorama import Fore, Style , init
load_dotenv()

init() #a required function for using  colorama(a styling library for python input function) on windows os
group_password=os.getenv('QUIZ_ACCESS_PASSWORD')

class Auth:
    
    def __init__(self):
        self.password=''
    def setPassword(self, password):
        self.password=password
    #compare for the equality of the password
    # #returns true if password matches alse returns false    
    def comparePassword (self):
         if group_password==self.password:
             return True 
         else:            
            return False 

 #this create an instance of an authentication  class and excute the authentication work flow
 #if the user couldn't provide a correct password after three attempts, application will quits    
def authenticateUSer ():
    auth= Auth()
    password=input(Style.NORMAL+'ENTER PASSWORD: ') #asks user to enter password
    auth.setPassword(password)
    i=1
    while i<3:
        if not auth.comparePassword():
            password=input('WRONG PASSWORD! ENTER PASSWORD AGAIN: ') #asks user to enter password
            auth.setPassword(password)
        elif auth.comparePassword:
            break
        i=i+1 #increment counter 

    if not auth.comparePassword():
        #exit application if user couldn't enter correct password after three attempts
        print(Fore.LIGHTRED_EX+'Password limit exceeded... Application is quited!')
        exit(1)    


    

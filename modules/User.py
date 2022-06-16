from errors.validation_error import NullInputError

#The class is for modelling an object/instance of a  user that intends to take a quiz
# The user class tracks the user performance while taking the quiz

user_instance=0
class User:
    #constructing and initiating class instance
    def __init__ (self, username, score):
        self.username=username  
        self.score=score
        global user_instance
        user_instance=user_instance+1
    
    #display name of user object
    def __str__ (self):
        return self.username
        
    
    #getter methods for user class 
    def getUsername(self):
        return self.username 
    def getScore(self):
        return self.score

    #setter methods for user class 
    def setUsername(self, username):
        self.username =username
    def setScore(self,score):
        self.score=score 

    #additional logic methods

    #reduceScore method helps reduce user score by the specified reduceBy parameter
    # the reduceBy parameter is an integer value to be deducted from the user score 
    def reduceScore(self, reduceBy):
        self.score= self.score-reduceBy



def initiateUser ():
    if user_instance==0:
        username=input('ENTER YOUR CHOICE USERNAME: ') #asks user to enter username
    else:
        username=input('Enter your choice username to return to the main page or enter "ctrl + c" to quit the game: ') #asks user to enter username
    if username =='':
        raise NullInputError('Username is required to start this game')   
    user = User(username,100)
    return user    

     


    

    

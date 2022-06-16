from utils import load_file_content_to_list as load_file 
from colorama import Fore, Style
from utils import load_score as load_score
from utils.clear_screen import clear_console_screen 
from math import ceil
import time

#the class for modelling quiz activities

class Quiz:
    def __init__(self, user):
        self.user=user #user  taking the quiz
        self.questions=[] #list of questions
        self.answers=[] #list of answers
        self.answeredQuestion=0 #number of correctly answered question
        self.unansweredQuestion=0 #number of unanswered questions
        self.question_with_wrong_answer=[] # stores the question the user fails with the correct answer
        self.last_wrong_answer='' #stores the last wrong answe from the user

    #start quiz by loading questions    
    def startQuiz(self):
        self.questions= load_file.load_file_content_to_list('external_files/questions.txt') #load questions from external file
        self.answers=load_file.load_file_content_to_list('external_files/answers.txt') #load answeres from external file

    #control question
    #the function returns true if user successfully answered all questions and vice versa
    def controlquiz (self):
        #loop through question to display for user
        k=1
        print('Loading questions...')
        time.sleep(2) #pause execution for 2 seconds
        clear_console_screen()
        for i, question in enumerate(self.questions):
            j=0
            #user is allowed to make another two attempts after wrong answer first attempt 
            while j<=3:
                if (j==3):
                    break
                global answer 
                answer=input(f"{i+1}. {question}: ") #display question
                if (answer.strip().lower()==self.answers[i].strip().lower()): #both the input answer and the program answer are converted to lower case 
                    print(Fore.LIGHTGREEN_EX+'\u2713 Correct Answer'+Style.RESET_ALL)
                    self.answeredQuestion=self.answeredQuestion+1 #increase the correctly answered question by 1
                    break
                elif (answer!=self.answers[i] and j==0):
                    self.user.reduceScore(1)
                    print(Fore.LIGHTRED_EX+'\u2718 Wrong Answer...You have two more attempts'+Style.RESET_ALL)
                elif (answer!=self.answers[i] and j==1):
                    self.user.reduceScore(2)
                    print(Fore.LIGHTRED_EX+'\u2718 Wrong Answer...You have one more attempt'+Style.RESET_ALL)
                elif (answer!=self.answers[i] and j==2):
                    self.user.reduceScore(3)
                    print(Fore.LIGHTRED_EX+'\u2718 Wrong Answer'+Style.RESET_ALL)
                j=j+1 #increase counter

            if (j==3): #quiz is forced to end after user reach guess limit
                self.question_with_wrong_answer=[question,self.answers[i]]
                self.last_wrong_answer=answer
                self.endQuiz()
                print(Fore.LIGHTMAGENTA_EX+f"Game ended! Sorry {self.user.username}, You have reached the guess limit. Kindly try again")
                displayCorrection(self)
                return False
        return True

                   

    #end quiz and save user score
    def endQuiz (self):
        self.unansweredQuestion= len(self.questions)-self.answeredQuestion
        self.user.score=ceil((self.answeredQuestion/len(self.questions)) * self.user.score) #compute final score by multipltin the fractionof answered question by the current score 
        load_score.load_score_to_file([self.user.username, self.user.score])

         
        

#function for initiating quiz  
def initiateQuiz(user):
    quiz= Quiz(user) #initiate quiz by passing the user object as argument
    quiz.startQuiz()
    isComplete=quiz.controlquiz()
    
    #check if user answer all questions to prevent duplicate call of endQuiz class method
    if isComplete:
        quiz.endQuiz()
    showUserScore(quiz)


def showUserScore(quiz):
    #clear_console_screen()
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+f'Hello {quiz.user.username}, here is your score'+Style.RESET_ALL)
    print('\n\t\t\t*************Quiz Score*******************\n')
    print(f'\t\t\t\tUsername: {quiz.user.username}\n')
    print(f'\t\t\t\tScore: {quiz.user.score}% of 100%\n')
    print(f'\t\t\t\tNo Of Correct Answers: {quiz.answeredQuestion}\n')
    print(f'\t\t\t\tNo Of unanswered questions: {quiz.unansweredQuestion}\n')
    print('\t\t\t******************************************')

def displayCorrection(quiz):
    #user is displayed with the questions he/she answered wrongly with the correct answers 
     print('\n\t\t\t*************Correction*******************\n')
     print(Fore.LIGHTGREEN_EX+'\n\tQuestion\n')
     print(f'\t\t{quiz.question_with_wrong_answer[0]}')
     print(Fore.LIGHTRED_EX+f'\n\tYour solution:{quiz.last_wrong_answer}\n')
     print(Fore.LIGHTGREEN_EX+f'\n\tCorrect solution:{quiz.question_with_wrong_answer[1]}\n')
    

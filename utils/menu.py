from modules.Quiz import initiateQuiz
from errors.validation_error import NullInputError
from modules.User import initiateUser
from utils.clear_screen import clear_console_screen
from colorama import init, Fore , Style
from utils.score_statistics import get_best_three_scores

#main menu page

def main ():
    #initiate the user with a username and assign user initial score
    user=None
    isUsernameEmpty=True
    while isUsernameEmpty:
        try:
            user=initiateUser()
            isUsernameEmpty=False
        except NullInputError as e:
            print(Fore.LIGHTRED_EX+e.errMsg+ Style.RESET_ALL)
    clear_console_screen() #clear console screen 
    welcomeUser(user.username)
    menu(user)  

#welcome component function            
def welcomeUser (username):
     print(Style.BRIGHT+ Fore.LIGHTBLUE_EX+ f'\t\t****Welcome {username}****\n')
     print(Fore.LIGHTBLACK_EX + '\t##################Options#############\n'+ Style.RESET_ALL)
 
#menu item component function 
def menu(user):
    print('1. Start Quiz')
    print('2. Go to score board')
    option=int(input('\nKindly enter the option number: '))
    if option==1:
        initiateQuiz(user)
    elif option==2:
        scoreBoard(user.username)
    else:
        print ('Invalid Input!')

def scoreBoard (username):
    clear_console_screen()
    print(Style.BRIGHT+ Fore.LIGHTBLUE_EX+ f'\t\t****Hi {username}, Welcome to scoreboard****\n')
    print(Fore.LIGHTBLACK_EX + '\tBelow is the list of the best three students with the highest scores\n'+ Style.RESET_ALL)
    scores=get_best_three_scores()
    if len(scores)<1:
        print(Fore.LIGHTBLACK_EX + f'\t\tNo quiz has been taken yet\n'+ Style.RESET_ALL)
        return
    for i, score in  enumerate(scores):
        print(Fore.LIGHTBLACK_EX + f'\t\t{i+1}. Username:{score[0]}  score:{score[1]}\n'+ Style.RESET_ALL)


    


   
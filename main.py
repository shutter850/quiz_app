
from colorama import init, Fore , Style
from utils.menu import main
from modules.Auth import authenticateUSer
import signal
import sys

#Main program file

init() #a required function for using  colorama(a styling library for python input function) on windows os
print(Style.BRIGHT+ Fore.LIGHTBLUE_EX+ '\t\t****Welcome to quiz question apps****')
print (Fore.LIGHTBLACK_EX + '\tKindly Note that only authorized users are allowed to participate in this quiz..Thanks!\n\n')

#handle signal to quit quiz
def signal_handler(sig, frame):
    print(Fore.LIGHTGREEN_EX+ Style.BRIGHT+'\n\t\t Bye for now.........Game quit!!'+Style.RESET_ALL)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


#authenticate user
authenticateUSer()
#start main 
while 1:
    main()
import os
import platform

#this file contains a function for  clearing console screen 
def clear_console_screen ():
    #check if code is running on windows
    if(platform.system()=='Windows'):
        os.system('cls') #cls is used for clearing screen in windows

    #clear is used for linux and mac os 
    else:  
        os.system('clear')
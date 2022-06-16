### About project
  A quiz game python program/application where user with access password can take quiz. Users are allowed to make two more quesses after inputing wrong answer. The game ends when the user reached the guessed limit or when user has successfully answered all questions. The user is shown his/her score when the game ends with the correction if game ends when an incorrect answer is given. The user starts by entering the group password, then the user is taken to the menu page where we have two options. the first option is to start the quiz, while the second option is to view the best three users with the highest socres. The game and educative, try the program and enjoy! 
### How to run
  Running this program/application requires python3 and  above  for accurate and nice experience. Running the program on the system different to the development/programmers's system requires the installation of external modules/libraries with the help of pip python package manager. Use 'python3 main.py' command on your terminal (macOS and linux ) or command line (windows) to start the program. Before entering the command, make sure to be in the root folder directory of this project.  

### Project features
 1. Student can take quiz questions
 2. Only Authorized user with password access can take quiz
 3. There won't be an individual password for each student but a group password
 4. The answer to the questions will be stored in an external file
 5. A user can only make three guesses for each question. After three attempts for a question, the user fails and quiz is quited

 6. At the start of the quiz, each user will be assigned a max point then on answering incorrect question, points will be deducted from the total assigned point.

 7. Game will end when user successfully answered every questions correctly then the score will be displayed.
 8. There will be a scoreboard where the score of the best three students will be displayed seperately
 9. Prefereable text color is  light blue, brown and black
 10. A hint of the correct answer will also be displayed e.g first letter of the correct solution
 11. While inputing the password, the no of attempts should be 3 


### Implementation

The program  has have three main sections
 * The authentication section
 * The quiz section
 * And the scoreboard section

 ##### Error classes 
   The Application has one custom error class- ValidationError

 ### Libraries and frameworks used
  1. Pyunit (for testing)
  2. python inbuilt file module
  3. unittest python inbuilt library 
  4. colorama
  5. csv
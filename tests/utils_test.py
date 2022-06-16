import unittest
from utils.load_file_content_to_list import  load_file_content_to_list
from utils.load_score import load_score_from_file

#unittest.TestCase child class for testing the various utils functions
class UtilUnitTest (unittest.TestCase):
    def test_the_lenght_of_question_list_should_be_10 (self):
        questions_list=load_file_content_to_list('external_files/questions.txt')
        self.assertEqual(len(questions_list), 10 , 'Something is wrong with load_file_content_to_list function')
    def test_the_lenght_of_questin_list_should_be_10 (self):
        questions_list=load_file_content_to_list('external_files/questions.txt')
        self.assertEqual(len(questions_list), 10 , 'Something is wrong with load_file_content_to_list function')
    def test_function_should_return_lenght_of_scores_in_external_file (self):
        scores=load_score_from_file()
        self.assertEqual(len(scores), 0, '''length of scores does not tally with scores external file content\n 
        Kindly change the number of expected length of the user scores to return to the equivalent length in the score_records.csv file in external_files folder''')
    
        
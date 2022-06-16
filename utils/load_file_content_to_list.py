
#loading of answers and questions are done here by reading the external file content to a list then returning the list
# to the caller
 
#the function below it takes one parameter which is the filename
def load_file_content_to_list(file_name):
    with open (file_name, 'r') as f:
        global content_list
        content_list=f.readlines()
    return content_list
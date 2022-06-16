import csv


#the load_score_to_file function write an list object (score and username) to a csv file called
#score_records.csv
#takes an argument of the list object
def load_score_to_file (data):
    with open ('external_files/score_records.csv' , 'a') as f:
        writer= csv.writer(f)
        writer.writerow(data)


def load_score_from_file ():
    scores=[]
    with open ('external_files/score_records.csv' , 'r') as f:
        reader= csv.reader(f)
        for i,row in enumerate(reader):
            if (i==0):
                continue
            try:
                refactor_row=[row[0], float(row[1])] #convert each score from string to row
                scores.append(refactor_row)
            except Exception as e:
                continue  
    return scores

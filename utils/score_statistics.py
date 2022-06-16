from utils.load_score import load_score_from_file
#statistical analysis involving score sorting of highest score to lowest score is done here

#sort scores list loaded form scores external csv file
def sortByScore (): 
    def sortCriteria(e):
        #sort by the value of the second item of the list object passed in descending order
        return e[1]
    scores=load_score_from_file()
    scores.sort(reverse=True, key=sortCriteria)
    return scores

#return the list of the best three users in terms of their scores
def get_best_three_scores():
    scores=sortByScore()
    best_three=[]
    for i, score in enumerate(scores):
        if (i>2):
            #stop lopping if the counter is greater than two i.e get only the best three students with the highest score from index 0-2
            break
        best_three.append(score)
    return best_three


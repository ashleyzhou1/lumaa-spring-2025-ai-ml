import sys
from cut_dataset import load_data
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def recommend_movies(user_input, dataset, top_n=5):
    
    #load dataset and preprocess text
    df = load_data(dataset)
    overviews = df['overview']
    score_diffs = {}

    #get sentiment score of user input
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores_user = analyzer.polarity_scores(user_input)
    compound_score_input =  sentiment_scores_user['compound']

    #loop through first 45 movies in dataset
    for i in range(0,45):
        #calculate sentiment score for each movie overview
        single_overview = df.iloc[i]['overview'] 
        sentiment_scores = analyzer.polarity_scores(single_overview)
        compound_score = sentiment_scores['compound']
        
        #calculate difference
        diff = compound_score_input-compound_score
        score_diffs[i] = abs(diff)
    sorted_diffs = dict(sorted(score_diffs.items(), key=lambda item: item[1]))
    
    #print movies with top 5 lowest differences
    count = 1;
    for key in sorted_diffs:
        if count>5:
            break
        print(str(count)+". "+df.iloc[key]['title'])
        print("Sentiment Score Difference: "+str(sorted_diffs[key])+"\n")
        count+=1; 

input = sys.argv[1]
recommend_movies(input, 'TMDB.csv')
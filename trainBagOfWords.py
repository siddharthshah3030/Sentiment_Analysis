# Import the pandas package, then use the "read_csv" function to read
# the labeled training data


import pandas as pd       
from bs4 import BeautifulSoup    
import re
import nltk
from nltk.corpus import stopwords # irrelevant words

train = pd.read_csv("labeledTrainData.tsv", header=0, \
                        delimiter="\t", quoting=3)

def clean(review):

    
    # beautifulSoup import and removal of HTML tags
    
    example1 = BeautifulSoup(train["review"][0])  
    #print(train["review"][0])
    #print(example1.get_text())
    
    #import re to remove numbers and other expressions except a-z
    letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                          " ",                   # The pattern to replace it with
                          example1.get_text() )  # The text to search
    
    #print (letters_only)
    
    lower_case = letters_only.lower()        # Convert to lower case
    words = lower_case.split()               # Split into words
    
    # nltk.download()  # Download text data sets, including stop words
    stops = set(stopwords.words("english"))
    
    #print (stopwords.words("english") )
    # removes non relevant englis words from word
    words = [w for w in words if not w in stops]
    #print( words)
    return( " ".join( words ))   
    
    
clean("Damn awesome SID")    


num_reviews = train["review"].size
clean_train_reviews = []

for i in range( 0, num_reviews ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( clean( train["review"][i] ) )


from sklearn.feature_extraction.text import CountVectorizer

# Initialize the "CountVectorizer" object, which is scikit-learn's
vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000) 


features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an 
# array
features = features.toarray()

# using random forect for classification on test set

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 100) 
forest = forest.fit( features, train["sentiment"] )




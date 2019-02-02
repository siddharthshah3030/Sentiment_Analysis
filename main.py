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
    print(train["review"][0])
    print(example1.get_text())
    
    #import re to remove numbers and other expressions except a-z
    letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                          " ",                   # The pattern to replace it with
                          example1.get_text() )  # The text to search
    
    print (letters_only)
    
    
    lower_case = letters_only.lower()        # Convert to lower case
    words = lower_case.split()               # Split into words
    
    # nltk.download()  # Download text data sets, including stop words
    
    print (stopwords.words("english") )
    # removes non relevant englis words from word
    words = [w for w in words if not w in stopwords.words("english")]
    print( words)
    return( " ".join( words ))   
    
    
clean("sid is hell")    
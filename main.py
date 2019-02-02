# Import the pandas package, then use the "read_csv" function to read
# the labeled training data
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0, \
                    delimiter="\t", quoting=3)

# beautifulSoup import and removal of HTML tags
from bs4 import BeautifulSoup    

example1 = BeautifulSoup(train["review"][0])  
print(train["review"][0])
print(example1.get_text())

#import re to remove numbers and other expressions except a-z
import re
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      example1.get_text() )  # The text to search

print (letters_only)


lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words
import os
import re
import sys
from bs4 import BeautifulSoup
import glob

inputDir = sys.argv[1]
outputDir = sys.argv[2]
print(outputDir)
entries = os.listdir(inputDir)
files = glob.glob("/"+outputDir +'*.txt')
counter = 0

for f in files:
    try:
        f.unlink()
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

def writeTokens(str, prefix):
    print(str)
    str_list = str.split()
    with open(prefix + 'tokens.txt','w') as log:
        for i in str_list:
            log.write('{}\n'.format(i))
    
def freq(str): 
    # break the string into list of words 
    str_list = str.split() 
    tokenDict = {}
    # gives set of unique words 
    unique_words = set(str_list) 

    # counting frequency of the words in set and storing in dict   
    for words in unique_words : 
        tokenDict[words] = str_list.count(words)

    # sorting the token dict in descending order
    sortedTokens = {k: v for k, v in sorted(tokenDict.items(), key=lambda item: item[1], reverse = True) }
    # writing tokens with frequency into log file
    with open('sortedTokens.txt','w') as log:
        for key in sortedTokens:
            log.write('{} {}\n'.format(key, sortedTokens[key]))
wholeString = ""
for i in entries:
    print("current file", counter)
    counter = counter + 1
    prefix = i.split(".")
    path = "/Users/akarshkashamshetty/OneDrive - UMBC/grad_sem4/CMSC676/project/" + inputDir + i

    with open(path, 'rb') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        text = soup.get_text()

    # converting all the characters into lower case
    text = text.lower()

    #cleaning the string by removing characters other than alphanumeric and spaces 
    cleanString = re.sub('[^A-Za-z0-9 ]+', '', text)
    wholeString = wholeString + cleanString
    writeTokens(cleanString, outputDir +"/"+ prefix[0])

freq(wholeString)


    
    
  

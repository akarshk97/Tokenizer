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
tokensDict = {}

def writeTokens(str, prefix):
    str_list = str.split()
    
    with open(prefix + 'tokens.txt','w') as f:
        for i in str_list:
            if i in tokensDict.keys():
                tokensDict[i] = tokensDict[i] + 1
            else:
                tokensDict[i] = 1

            f.write('{}\n'.format(i))
    f.close()
    
def freq(str): 
    counter = 0
    # break the string into list of words 
    str_list = str.split() 
    print(len(str_list))
    tokenDict = {}
    # gives set of unique words 
    unique_words = set(str_list) 
    print("unique words",len(unique_words))
    print("yes1")
    # counting frequency of the words in set and storing in dict   
    # for words in unique_words : 
    #     #print(counter)
    #     counter = counter + 1
    #     tokenDict[words] = str_list.count(words)
    print("yes2")
    # sorting the token dict in descending order
    sortedTokens = {k: v for k, v in sorted(tokensDict.items(), key=lambda item: item[1], reverse = True) }
    # sorting the freq of token in  dict in descending order
    sortedFreq = dict(sorted(tokensDict.items(), key=lambda x: x[0]))
    
    # writing tokens with frequency into log file
    with open('sortedFreq.txt','w') as f:
        for key in sortedTokens:
            f.write('{} {}\n'.format(key, sortedTokens[key]))
    f.close()
    with open('sortedTokens.txt','w') as ff:
        for key in sortedFreq:
            ff.write('{} {}\n'.format(key, sortedFreq[key]))
    ff.close()
wholeString = ""
for i in entries:
    print("current file", counter)
    counter = counter + 1
    prefix = i.split(".")
    path = "/Users/akarshkashamshetty/OneDrive - UMBC/grad_sem4/CMSC676/project/" + inputDir + i

    with open(path, 'rb') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        text = soup.get_text()
    fp.close()

    # converting all the characters into lower case
    text = text.lower()

    #cleaning the string by removing characters other than alphanumeric and spaces 
    cleanString = re.sub('[^A-Za-z ]+', '', text)
    wholeString = wholeString + cleanString
    writeTokens(cleanString, outputDir +"/"+ prefix[0])

freq(wholeString)


    
    
  

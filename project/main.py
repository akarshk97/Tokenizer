#Author : Akarsh Kashamshetty
#course : CMSC676
#term : Spring 2021

import os
import re
import sys
from bs4 import BeautifulSoup
import glob
import time

t1 = time.time()
c1 = time.process_time()
# reading input directory and output directory from command line
inputDir = sys.argv[1]
outputDir = sys.argv[2]

# getting the file names from the input directory as strings
entries = os.listdir(inputDir)

# cleaning files from the output directory initially
files = glob.glob("/"+outputDir +'*.txt')
counter = 0
for f in files:
    try:
        f.unlink()
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

# a global dictionary for storing tokens and frequency count
tokensDict = {}

# tokenizes the document and stores in a separete file for each file 
#Also updates the global tokensDict with the tokens frequency i.e calculating frequency
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
    

def sortWriteFiles(): 
    
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

# processing all the files in the input directory
for i in entries:
    #print("current file", counter)
    counter = counter + 1
    prefix = i.split(".")
    path = "/Users/akarshkashamshetty/OneDrive - UMBC/grad_sem4/CMSC676/project/" + inputDir + i

    try:
        with open(path, 'rb') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            # getting text from the html document using parser
            text = soup.get_text()
        fp.close()
    except:
        print("err")

    # converting all the characters into lower case
    text = text.lower()
    text.replace("'","")

    #cleaning the string by removing characters other than alphanumeric and spaces 
    cleanString = re.sub('[^A-Za-z ]+', ' ', text)
    
    writeTokens(cleanString, outputDir +"/"+ prefix[0])

sortWriteFiles()
t2 = time.time()
c2 = time.process_time()
print("Elapsed time",t2-t1)
print("CPU time", c2-c1)
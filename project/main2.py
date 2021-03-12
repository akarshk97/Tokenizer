#Author : Akarsh Kashamshetty
#course : CMSC676
#term : Spring 2021

import os
import re
import sys
from bs4 import BeautifulSoup
import glob
import time
from collections import defaultdict
import csv
import math


# reading input directory and output directory from command line
inputDir = sys.argv[1]
outputDir = sys.argv[2]

# getting the file names from the input directory as strings
entries = os.listdir(inputDir)

counter = 0
global count # for counting stopwords that went through preprocessing
count = 0
global counter3
counter3 = 0
global flag 
flag = False

# a global dictionary for storing tokens and frequency count
tokensDict = {}
stopWords = []
idf = {}
def readStopWords():
    with open('stopwords.txt', "r") as frs:
        stopwrds = frs.read().split()
    frs.close()
    for i in stopwrds:
        stopWords.append(i)
    print("in the readStop")
readStopWords()



def calTfIdf():
    outputEntries = os.listdir(outputDir)
    for entry in outputEntries:
        print(entry)
    counter3 = 0
    for i in outputEntries:
        print(counter3)
        counter3+=1
        with open("outputLog/" + i, "r") as file:
            rows = ( line.split(',') for line in file)
            dict = { row[0]:row[1] for row in rows }
            for item in dict:
                print(item," ",dict[item])    
        file.close()
        D = dict
        with open('outputLog2/'+i,'w') as ff:
            for k in D.keys():
                ff.write('{} {}\n'.format(k, D[k]))
            print(i)    
        ff.close()


    
# tokenizes the document and stores in a separete file for each file 
#Also updates the global tokensDict with the tokens frequency i.e calculating frequency
def writeTokens(str, prefix, numdocs):
    tokensDict = {}
    str_list = str.split()
    count = 0
    # not including the stop words into the tokenDict and measuring token freq for the rest
    for i in str_list:
        if i in stopWords:
            count += 1
            continue
        elif i in tokensDict.keys():
            tokensDict[i] = tokensDict[i] + 1
        else:
            tokensDict[i] = 1
    #removing words with freq 1 and length 1 
    for key in list(tokensDict):
        if tokensDict[key]==1:
            del tokensDict[key]
        if len(key) == 1:
            del tokensDict[key]
    # updating the number of documents containing the word for calc idf later
    if flag == False:
        for key in tokensDict.keys():
            if key in idf:
                idf[key] += 1
            else:
                idf[key] = 1
    totalWords = sum(tokensDict.values())
    # intially writing the tokens and thier tf into the .txt files
    if flag == True:
        with open(prefix + 'tokens.txt','w') as f:
            for i in tokensDict.keys():
                tf = tokensDict[i]/totalWords
            #tf = round(tf, 7)
                weight = tf * math.log(numdocs/idf[i])
                f.write('{},{}\n'.format(i, weight))
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

count = 0 
def readText(numdocs):
    counter = 0
    for i in entries[:numdocs]:
        counter += 1
    #print("current file", counter)
        counter = counter + 1
        prefix = i.split(".")
        path = "/Users/akarshkashamshetty/OneDrive - UMBC/grad_sem4/CMSC676/project/" + inputDir + i

    
        with open(path, 'rb') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            # getting text from the html document using parser
            text = soup.get_text()
        fp.close()
    
    # converting all the characters into lower case
        text = text.lower()
        text.replace("'","")

    #cleaning the string by removing characters other than alphanumeric and spaces 
        cleanString  = re.sub('-', '', text)
    #cleanString  = re.sub("'", '', text)
        cleanString = re.sub('[^A-Za-z ]+', ' ', text)
    
    
        writeTokens(cleanString, outputDir +"/"+ prefix[0], numdocs)

cputimes = []

for i in [10, 20, 40, 80, 100, 200, 300, 400, 500]:
    t1 = time.time()
    c1 = time.process_time()
    print("numdocs",i)
    flag = False
    readText(i)
#sortWriteFiles()
#calTfIdf()
    flag = True
    readText(i)
#print("counter2", count)
    t2 = time.time()
    c2 = time.process_time()
    cputimes.append(c2 - c1)
    print("Elapsed time",t2-t1)
    print("CPU time", c2-c1)
print(cputimes)
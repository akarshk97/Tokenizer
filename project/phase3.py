# Author : Akarsh Kashamshetty
#course : CMSC676
# term : Spring 2021
#phase : 2
# date : 12 March 2021

import os
import re
import sys
from bs4 import BeautifulSoup
import glob
import time
from collections import defaultdict
import csv
import math
import matplotlib.pyplot as plt


# reading input directory and output directory from command line
inputDir = sys.argv[1]
outputDir = sys.argv[2]

# getting the file names from the input directory as strings
entries = os.listdir(inputDir)

flag = False
# fileCounter
fileCounter = 0
postFileCount = 0
tokensSum = 0

# a global dictionary for storing tokens and frequency count
tokensDict = {}
tokensDict2 = {}
weights = {}
stopWords = []
idf = {}
dictFile = {}
postFile = {}


def readStopWords():
    with open('stopwords.txt', "r") as frs:
        stopwrds = frs.read().split()
    frs.close()
    for i in stopwrds:
        stopWords.append(i)


readStopWords()


# Tokenizes each document and appends the tokens into dictionary tokensDict
# Also updates the global tokensDict2 with the tokens frequency
def writeTokens(str, prefix, docId, numdocs):
    tokensDict = {}
    str_list = str.split()
    count = 0
    global tokensSum
    # not including the stop words into the tokenDict and measuring token freq for the rest
    for i in str_list:
        if i in stopWords:
            count += 1
            continue
        elif i in tokensDict.keys():
            tokensDict[i] = tokensDict[i] + 1
        else:
            tokensDict[i] = 1

    # removing words with freq 1 and length 1
    for key in list(tokensDict):
        if tokensDict[key] == 1:
            del tokensDict[key]
        if len(key) == 1:
            del tokensDict[key]
    # updating the number of documents containing the word for calc idf later
    if flag == False:
        for i in str_list:
            if i in stopWords:
                count += 1
                continue
            elif i in tokensDict2.keys():
                tokensDict2[i] = tokensDict2[i] + 1
            else:
                tokensDict2[i] = 1
        for key in list(tokensDict2):
            if tokensDict2[key] == 1:
                del tokensDict2[key]
            if len(key) == 1:
                del tokensDict2[key]
        for key in tokensDict.keys():
            if key in idf:
                idf[key] += 1
            else:
                idf[key] = 1
    tokensSum = tokensSum + len(tokensDict)
    totalWords = sum(tokensDict.values())
    # intially writing the tokens and thier tf into the .txt files
    if flag == True:
        global postFileCount
        for i in tokensDict.keys():
            tf = tokensDict[i]/totalWords
            weight = tf * math.log(numdocs/idf[i])
            postFile[postFileCount] = [i, docId, weight]
            postFileCount += 1


def sortWriteFiles():
    # sorting the token dict in descending order
    sortedTokens = {k: v for k, v in sorted(
        tokensDict2.items(), key=lambda item: item[1], reverse=False)}
    count = 1
    # writing tokens with frequency into log file
    x = list(range(1, len(sortedTokens)+1))
    y = list(sortedTokens.values())
    plt.loglog(x, y)
    plt.xlabel('rank')
    plt.ylabel('frequencies')
    plt.show()
    with open('sortedFreq.txt', 'w') as f:
        for key in sortedTokens:
            f.write('{} {}\n'.format(key, sortedTokens[key] * count))
            count = count + 1
    f.close()

# processing all the files in the input directory


def readText(numdocs):
    counter = 0
    for i in entries[:numdocs]:
        counter += 1
        print("current file", counter)
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
        text.replace("'", "")

    # cleaning the string by removing characters other than alphanumeric and spaces
        cleanString = re.sub('-', '', text)
    #cleanString  = re.sub("'", '', text)
        cleanString = re.sub('[^A-Za-z ]+', ' ', text)
        writeTokens(cleanString, outputDir + "/" +
                    prefix[0], prefix[0], numdocs)


def writeFiles(dict1, dict2, fCounter):

    with open(outputDir + str(fCounter)+'dictionaryFile.txt', 'w') as f:
        for k in dict1.keys():
            f.write('{}\n'.format(k))
            f.write('{}\n'.format(dict1[k][0]))
            f.write('{}\n'.format(dict1[k][1]))
    with open(outputDir + str(fCounter)+'postingsFile.txt', 'w') as ff:
        for key in dict2.keys():
            ff.write('{},{},{}\n'.format(
                dict2[key][0], dict2[key][1], dict2[key][2]))
        f.close()
        ff.close()



cputimes = []

#[10, 20, 40, 80, 100, 200, 300, 400, 500]
for i in [503]:
    t1 = time.time()
    c1 = time.process_time()
    print("numdocs", i)

    flag = False
    readText(i)

    flag = True
    readText(i)
    fileCounter += 1
    #postFile = dict(sorted(postFile.items()))
    postFile = dict(sorted(postFile.items(), key=lambda e: e[1][1]))
    print("postFile length :",len(postFile))
    print("len of tokensdict2", len(tokensDict2))
    print("sun of toeknsdict2 values",sum(tokensDict2.values()))
    print("toekns SUn", tokensSum)
    print("len of idf",len(idf))
    count = 0
    pos = 0
    for k in idf.keys():
        count = 0
        for word in postFile.keys():
            count += 1
            if k == postFile[word][0]:
                pos = count
                break
        dictFile[k] = [idf[k], pos]
    dictFile = dict(sorted(dictFile.items()))

    #writeFiles(dictFile, postFile, fileCounter)
    t2 = time.time()
    c2 = time.process_time()
    cputimes.append(c2 - c1)
    print("Elapsed time", t2-t1)
    print("CPU time", c2-c1)
print(cputimes)

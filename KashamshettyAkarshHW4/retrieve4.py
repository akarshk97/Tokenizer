# Author : Akarsh Kashamshetty
#course : CMSC676
# term : Spring 2021
#phase : 4
# date : 16 April 2021

import sys
import re

wordList = []
weightList = []
docDict = {}

postings = {}
dictList = {}
# reading postings and dictionary list from disk

# loading postings list into memory
pFile = open('output1dict1postingsFile.txt','r')
dFile = open('output1dictionaryFile.txt', 'r')
lines = pFile.readlines()
count = 1

for line in lines:
    val1, val2 = line.split(',')
    postings[count] = [val1.strip(), val2.strip()] 
    count += 1
# loading dictionary list or index file into memory
lines = dFile.readlines()
count = 1
for line in lines:
    if count%3==1:
        key = line.strip()
    elif count%3==2:
        val1 = int(line)
    else:
        val2 = int(line)
        dictList[key] = [val1, val2]
    count += 1

#wordList - terms to retrieve
cmdCount = 1
if sys.argv[1] == 'Wt':
    for i in sys.argv[2:]:
        if cmdCount%2 == 0:
            wordList.append(i)
        else:
            weightList.append(i)
        cmdCount+=1
else:
    for i in range(len(sys.argv)-1):
        wordList.append(sys.argv[i+1])
        weightList.append(1)

#print(weightList)
#print(wordList)

    
# term dictionary with term and list is lists of document id and weight
words = {}
for wrd in wordList:
    #preprocessing
    wrd = wrd.lower()
    wrd = re.sub('[^A-Za-z ]+', '', wrd)
    #if the word not in dictionary file continue
    if wrd not in dictList.keys():
        continue
    loc = dictList[wrd][1]
    freq = dictList[wrd][0]
    for i in range(freq):
        if wrd in words.keys():
            words.get(wrd).append(postings[i + loc])
        else :
            words[wrd] = [postings[loc]]

#documenets dictionary with sum of weights of the terms
docDict = {}
#print("wordkeys",words.keys())
wCount = 0
for value in words.values():
    for val in value:
        docDict[val[0]] = (docDict[val[0]] + (float(val[1])  * float(weightList[wCount]))) if (val[0] in docDict.keys()) else float(val[1]) * float(weightList[wCount])
    wCount += 1

# sorting the dictionary in descending order of the weights
docDict = dict(sorted(docDict.items(), key = lambda e : e[1], reverse = True))
finalCounter = 0

# output to the termimal with top ten documents 
for docId in docDict.keys():
    finalCounter+=1
    print(docId + ".html", docDict[docId])
    if finalCounter == 10:
        break

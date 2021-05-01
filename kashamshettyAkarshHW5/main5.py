#Author : Akarsh Kashamshetty
#course : CMSC676
#term : Spring 2021
#phase : 5
#date : 30 April 2021


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
import spacy 
nlp = spacy.load('en_core_web_sm')

import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.cluster import AgglomerativeClustering


from sklearn.neighbors.nearest_centroid import NearestCentroid

import en_core_web_sm
nlp = en_core_web_sm.load()


# reading input directory and output directory from command line
inputDir = sys.argv[1]

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
#tokensDict2 = {}
weights = {}
stopWords = []
docWords = {}
#idf = {}

vectorizer = TfidfVectorizer()

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]
    
def readStopWords():
    with open('stopwords.txt', "r") as frs:
        stopwrds = frs.read().split()
    frs.close()
    for i in stopwrds:
        stopWords.append(i)
readStopWords()

    
# tokenizes the document and stores in a separete file for each file 
#Also updates the global tokensDict with the tokens frequency i.e calculating frequency
def writeTokens(str1, prefix, numdocs):
    tokensDict = {}
    str_list = str1.split()
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
    listToStr = ' '.join([str(elem) for elem in tokensDict.keys()])
    docWords[prefix] = listToStr



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
    
    
        writeTokens(cleanString, "/"+ prefix[0], numdocs)

cputimes = []
t1 = time.time()
c1 = time.process_time()
#[10, 20, 40, 80, 100, 200, 300, 400, 500]
for i in [503]:
    print("numdocs",i)
    readText(i)

    
    

maxSim = 0
minSim = 1
for doc1 in docWords.keys():
    for doc2 in docWords.keys():
        if doc2 == doc1:
            continue
        ndoc1 = nlp(docWords[doc1])
        ndoc2 = nlp(docWords[doc2])
        sim = docWords[doc1].similarity( docWords[doc2])
        if maxSim < sim:
            maxSim = sim
            maxsimdoc11name = doc1
            maxsimdoc22name = doc2
        if minSim > sim:
            minSim = sim
            minsimdoc11name = doc1
            minsimdoc22name = doc2


clustering = AgglomerativeClustering().fit(docWords.values())
print(clustering.labels_)

t2 = time.time()
c2 = time.process_time()
cputimes.append(c2 - c1)
print("Elapsed time",t2-t1)
print("CPU time", c2-c1)

print(maxsimdoc11name," and ",maxsimdoc22name, " are Maximum similar documents with similarity of ",maxSim,)
print(minsimdoc11name," and ",minsimdoc22name, " are most dissimilar documents with similarity of ",minSim,)


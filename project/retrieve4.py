import sys

wordList = []
docDict = {}

postings = {}
dictList = {}
# reading postings and dictionary list from disk
#postings
pFile = open('outputdup1postingsFile.txt','r')
dFile = open('outputdup1dictionaryFile.txt', 'r')
lines = pFile.readlines()
count = 1

for line in lines:
    val1, val2 = line.split(',')
    postings[count] = [val1.strip(), val2.strip()] 
    count += 1
#dictList
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

#wordList - words to retrieve
for i in range(len(sys.argv)-1):
    wordList.append(sys.argv[i+1])



words = {}
for wrd in wordList:
    if wrd not in dictList.keys():
        continue
    loc = dictList[wrd][1]
    freq = dictList[wrd][0]
    #print(postings[loc])
    for i in range(freq):
        if wrd in words.keys():
            words.get(wrd).append(postings[i + loc])
        else :
            words[wrd] = [postings[loc]]

#print(words)
docDict = {}
for value in words.values():
    for val in value:
        docDict[val[0]] = (docDict[val[0]] + float(val[1])) if (val[0] in docDict.keys()) else float(val[1])
# print(docDict)

docDict = dict(sorted(docDict.items(), key = lambda e : e[1], reverse = True))
finalCouter = 0
for docId in docDict.keys():
    finalCouter+=1
    print(docId, docDict[docId])
    if finalCouter == 10:
        break








# # creating docList with all the documents containing words
# for word in wordList:
#     if word in dictList.keys():
#         loc = dictList[word][1]
#         for i in range(dictList[word][0]):
#             docList.append(postings[loc + i][0])
# # print(docList)
# docIdSortedPostings = {}
# docIdSortedPostings = dict(sorted(postings.items(), key = lambda e : e[1][0]))
# wordList = sorted(wordList)
# # flag for knowing when to break from searching docid
# flag = False
# #sorting wordlist for easy search
# for idx in docList: 
#     print(idx)
#     for i in range(1,len(docIdSortedPostings)):
#         dCount = i
#         count = 0
#         print(docIdSortedPostings[dCount][1])
#         while docIdSortedPostings[dCount][0] == idx and dCount < len(docIdSortedPostings):
#             print(1)
#             if docIdSortedPostings[dCount][0] == wordList[count] and count < len(wordList):
#                 print(2)
#                 docDict[idx] =  docDict[idx].append(docIdSortedPostings[i][2]) if (idx in docDict.keys()) else [docIdSortedPostings[i][2]]
#                 count+=1
#             dCount+=1
#             flag = True
#         if flag == True:
#             print(3)
#             break

# print(docDict)
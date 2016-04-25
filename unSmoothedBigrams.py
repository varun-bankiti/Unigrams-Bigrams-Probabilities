""" Author: Varun Kumar Reddy B
    Question 3
    Homework 1
    CS 6320 Fall'15 """

import collections
from operator import itemgetter

corpusFileName="corpus.txt" 
corpusFile=open(corpusFileName);
data=corpusFile.read()
corpusTokens=data.split()
noOfTokens=(float)(len(corpusTokens))

## Reading the Tokens from the File

tokenFileName="inputTokens.txt" 
tokenFile=open(tokenFileName);
tokens=[x[:-1] for x in tokenFile.readlines()]


## Unigrams Proababilities Calculation  

unSmoothedUnigrams={}
for token in tokens:
    unSmoothedUnigrams[token]=corpusTokens.count(token)
    
## Writing Unigrams Probabilites to File

unigramFileName="unSmoothedUnigrams.txt"
unigramFile=open(unigramFileName,"w")
orderedUnSmoothedUnigrams = collections.OrderedDict(sorted(unSmoothedUnigrams.items(), key=itemgetter(0)))
for token in orderedUnSmoothedUnigrams.keys():
    unigramFile.write(token+" %.9f" % (orderedUnSmoothedUnigrams[token]/noOfTokens) +"\n")
    
## Bigrams Proababilities Calculation    
    
unSmoothedBigrams={}
prevWord=tokens[0]
for index in range(1,len(tokens)):
    bigram=prevWord+" "+tokens[index]
    val=0
    for i in range(len(corpusTokens)-1):
        if(corpusTokens[i]==prevWord and corpusTokens[i+1]==tokens[index]):
            val+=1
    unSmoothedBigrams[bigram]=val
    prevWord=tokens[index]
    
## Writing Bigrams Probabilites to File    

bigramFileName="unSmoothedBigrams.txt"
bigramFile=open(bigramFileName,"w")
for x in orderedUnSmoothedUnigrams.keys():
    for y in orderedUnSmoothedUnigrams.keys():
        word=x+" "+y
        if word in unSmoothedBigrams:
            bigramFile.write(word+" %.9f" % (unSmoothedBigrams[word]/(float)(unSmoothedUnigrams[x]))+"\n")
        else:
            bigramFile.write(word+" 0\n")

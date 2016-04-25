""" Author: Varun Kumar Reddy B
    Question 3
    Homework 1
    CS 6320 Fall'15 """
    
import collections
from operator import itemgetter 

## Reading the Tokens from the File
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
smoothedUnigrams={}
for token in tokens:
    smoothedUnigrams[token]=corpusTokens.count(token)   

## Unigrams Counts Smoothing
        
unigramsCounts=[0 for x in range(int(noOfTokens)+1)]

unigramsMaxCount=-1
for token in smoothedUnigrams:
    unigramsCounts[smoothedUnigrams[token]]+=1
    unigramsMaxCount=max(unigramsMaxCount,smoothedUnigrams[token])
unigramsSmoothedCounts=[0.0 for x in range(unigramsMaxCount+1)]
for i in range(1,unigramsMaxCount+1):
    if(unigramsCounts[i]>0):
        if(unigramsCounts[i+1]==0):
            for j in range(i+1,unigramsMaxCount+1):
                if(unigramsCounts[j]!=0):
                    unigramsSmoothedCounts[i]=((i+1.0)*(float(unigramsCounts[j])))/float(unigramsCounts[i])
                    break;
        else:
            unigramsSmoothedCounts[i]=((i+1.0)*(float(unigramsCounts[i+1])))/float(unigramsCounts[i])
unigramsSmoothedCounts[0]=unigramsSmoothedCounts[1]
for i in smoothedUnigrams:
    smoothedUnigrams[i]=unigramsSmoothedCounts[smoothedUnigrams[i]]

## Writing Unigaram Probabilites to File

orderedSmoothedUnigrams = collections.OrderedDict(sorted(smoothedUnigrams.items(), key=itemgetter(0)))
unigramFileName="smoothedUnigrams.txt"
unigramFile=open(unigramFileName,"w")
for token in orderedSmoothedUnigrams.keys():
    unigramFile.write(token+" %.9f" % (orderedSmoothedUnigrams[token]/noOfTokens) +"\n")
    
## Bigrams Proababilities Calculation

smoothedBigrams={}
prevWord=tokens[0]
for index in range(1,len(tokens)):
    bigram=prevWord+" "+tokens[index]
    val=0
    for i in range(len(corpusTokens)-1):
        if(corpusTokens[i]==prevWord and corpusTokens[i+1]==tokens[index]):
            val+=1
    smoothedBigrams[bigram]=val
    prevWord=tokens[index]

## Bigrams Counts Smoothing

bigramsCounts=[0 for x in range(int(noOfTokens)+1)]
bigramsMaxCount=-1
for token in smoothedBigrams:
    bigramsCounts[smoothedBigrams[token]]+=1
    bigramsMaxCount=max(bigramsMaxCount,smoothedBigrams[token])

bigramsSmoothedCounts=[0.0 for x in range(bigramsMaxCount+1)]
for i in range(1,bigramsMaxCount+1):
    if(bigramsCounts[i]>0):
        if(bigramsCounts[i+1]==0):
            for j in range(i+1,bigramsMaxCount+1):
                if(bigramsCounts[j]!=0):
                    bigramsSmoothedCounts[i]=((i+1.0)*(float(bigramsCounts[j])))/float(bigramsCounts[i])
                    break;
        else:
            bigramsSmoothedCounts[i]=((i+1.0)*(float(bigramsCounts[i+1])))/float(bigramsCounts[i])

bigramsSmoothedCounts[0]=bigramsSmoothedCounts[1]
for i in smoothedBigrams:
    smoothedBigrams[i]=bigramsSmoothedCounts[smoothedBigrams[i]]
orderedSmoothedBigrams = collections.OrderedDict(sorted(smoothedBigrams.items(), key=itemgetter(0)))

## Writing Bigram Probabilities to File

bigramFileName="smoothedBigrams.txt"
bigramFile=open(bigramFileName,"w")
for x in orderedSmoothedUnigrams.keys():
    for y in orderedSmoothedUnigrams.keys():
        word=x+" "+y
        if word in orderedSmoothedBigrams:
            if(orderedSmoothedUnigrams[x]!=0):
                bigramFile.write(word+" %.9f" % (orderedSmoothedBigrams[word]/(float)(orderedSmoothedUnigrams[x]))+"\n")
            else:
                bigramFile.write(word+" "+str(bigramsSmoothedCounts[0]/float(noOfTokens))+"\n")                
        else:
            bigramFile.write(word+" "+str(bigramsSmoothedCounts[0]/float(noOfTokens))+"\n")

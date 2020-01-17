# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:10:56 2018

@author: Marcus
Using beginner tutorial by Rachael Tatman from Kaggle
"""

# read in some helpful libraries
import nltk # the natural langauage toolkit, open-source NLP
import pandas as pd # dataframes
from time import time

startTime = time()
### Read in the data

# read our data into a dataframe
trainData = pd.read_csv("train/train_train.csv")
testData = pd.read_csv("train/train_test.csv")
#testData = pd.read_csv("train/train_test-tiny.csv")

# look at the first few rows
print ("TrainData:")
print (trainData.head() )
print ("TestData:")
print (testData.head() )

### Test using parsed data:
testAuthors = testData.head().author
for author in testAuthors:
    print ("Author: ", author)

testAuthors = testData.head().author
testText = testData.head().text

for author in range(len(testAuthors)):
    print ("Author: ", testAuthors[author])
    print ("Sentence: ", testText[author])

### Split data
'''
# split the data by author
byAuthor = trainData.groupby("author")

### Tokenize (split into individual words) our text

# word frequency by author
wordFreqByAuthor = nltk.probability.ConditionalFreqDist()

# for each author...
for name, group in byAuthor:
    # get all of the sentences they wrote and collapse them into a
    # single long string
    sentences = group['text'].str.cat(sep = ' ')
    
    # convert everything to lower case (so "The" and "the" get counted as 
    # the same word rather than two different words)
    sentences = sentences.lower()
    
    # split the text into individual tokens    
    #sentences=nltk.sent_tokenize(sample.decode('utf-8'))
    tokens = nltk.tokenize.word_tokenize(sentences.decode('utf-8'))
    
    # calculate the frequency of each token
    frequency = nltk.FreqDist(tokens)

    # add the frequencies for each author to our dictionary
    wordFreqByAuthor[name] = (frequency)
    
# now we have an dictionary where each entry is the frequency distribution
# of words for a specific author. 

# One way to guess authorship is to use the joint probabilty that each 
# author used each word in a given sentence.


success = 0
mistake = 0
testAuthor = testData.author
testSentence = testData.text

### Run this for each sentence:

for sentence in range (len(testSentence)):
    # create an empy dataframe to put our output in
    testProbabilities = pd.DataFrame(columns = ['author','word','probability'])
    yStar = testAuthor[sentence]
    #print (yStar, " : ", testSentence[sentence])
    decodedSentence = testSentence[sentence].decode('utf-8')
    preProcessedTestSentence = nltk.tokenize.word_tokenize(decodedSentence.lower())

    #preProcessedTestSentence = nltk.tokenize.word_tokenize(testSentence[sentence].lower())
    # For each author...
    for i in wordFreqByAuthor.keys():
        # for each word in our test sentence...
        for j  in preProcessedTestSentence:
            # find out how frequently the author used that word
            wordFreq = wordFreqByAuthor[i].freq(j)
            # and add a very small amount to every prob. so none of them are 0
            smoothedWordFreq = wordFreq + 0.000001
            # add the author, word and smoothed freq. to our dataframe
            output = pd.DataFrame([[i, j, smoothedWordFreq]], columns = ['author','word','probability'])
            testProbabilities = testProbabilities.append(output, ignore_index = True)
    
    # empty dataframe for the probability that each author wrote the sentence
    testProbabilitiesByAuthor = pd.DataFrame(columns = ['author','jointProbability'])
    
    # now let's group the dataframe with our frequency by author
    for i in wordFreqByAuthor.keys():
        # get the joint probability that each author wrote each word
        oneAuthor = testProbabilities.query('author == "' + i + '"')
        jointProbability = oneAuthor.product(numeric_only = True)[0]
        
        # and add that to our dataframe
        output = pd.DataFrame([[i, jointProbability]], columns = ['author','jointProbability'])
        testProbabilitiesByAuthor = testProbabilitiesByAuthor.append(output, ignore_index = True)
    
    # and our winner is...
    yHat = testProbabilitiesByAuthor.loc[testProbabilitiesByAuthor['jointProbability'].idxmax(),'author']

    if yHat == yStar:
        success += 1
    else:
        mistake += 1
        

successRate = 100 * float (success)/len(testData)
testTime = time() - startTime

print ("mistakes = ", mistake, "success rate = ", successRate, "  run time: ", testTime)
'''
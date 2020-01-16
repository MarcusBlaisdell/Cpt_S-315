########################
### Marcus Blaisdell
### Cpt_S 315
### Homework #3
###
### HW3_FC_Class.py
###
########################

########################
### 1. initialize the weights, w = 0
### 2. for each training iteration, do:
### 3.    for each training example, do:
### 4.       yHat = sign(w*xt) // predict using current weights
### 5.       if mistake, then
### 6.          w = w + eta * yt * xt // update the weights
### 7.       end if
### 8.    end for
### 9. end for
### 10. return final weight vector w
###
########################

import numpy as np
from HW3_Functions import sign

class FCookie():
    ### attributes:
        # dictionary let's us utilize the hash functions for faster searching
    stopList = {}
        # lists to utilize indexing:
    trainData = []
    trainLabel = []
    testData = []
    testLabel = []
    vocabulary = []
    featureVectorList = []
    eta = 1 # learning ratingIndex
    w = np.array([0]) # weight vector
    m = 0

        ### initialize the class:
    def __init__(self):
        pass
    ### end __init__

    ### readStops function
    ### read the words from the stoplist text fileName
    ### into a dictionary
    ### the dictionary makes it faster to search
    ### whether or not a word is in the stoplist or not

    def readStops(self, fileName):
        inFile = open (fileName, "r")

        string = ''
        word = ''

        string = inFile.readline()

        while string:
            for letter in range(len(string)):
                if letter == len(string) - 1:
                    if string[letter] != '\r' and string[letter] != '\n':
                        word += string[letter]
                    ### if the word is not in the dictionary, add it, else,
                    ### no action required
                    if self.stopList.get(word, 'n') == 'n':
                        self.stopList[word] = 1
                    word = ''
                elif letter == ' ':
                    self.stopList.append(word)
                    word = ''
                else:
                    word += string[letter]

            string = inFile.readline()

        inFile.close()
    ### end readStops

    ### read the fortunes into a list for processing:

    def readLines(self, fileName, dataName):
        inFile = open (fileName, "r")

        lineList = []
        word = ''

        string = inFile.readline()

        while string:

            for letter in range(len(string)):
                if letter == len(string) - 1:
                    lineList.append(word)
                    dataName.append (lineList)
                    lineList = []
                    word = ''
                elif string[letter] == ' ':
                    lineList.append(word)
                    word = ''
                else:
                    word += string[letter]

            string = inFile.readline()

        inFile.close()

    ### end readLines

    ### read the labels into a list for processing
    ### it will be assumed that the line numbers of the labels
    ### match the line numbers of the training data

    def readLabels(self, fileName):
        inFile = open (fileName, "r")

        lineList = []
        word = ''

        string = inFile.readline()

        while string:
            self.trainLabel.append (string[0])
            string = inFile.readline()
        inFile.close()

    ### end readLabels

    ### initializeWeight function
    def initializeWeight (self):
        self.m = len(self.vocabulary)
        self.w = np.zeros(self.m, dtype=int)
    ### end initializeWeight function

    ### perceptron function:

    def perceptron (self):
        ### initialize variables
        ### initialize prediction (yHat) and actual (yStar) to (0)
        ### use numpy for vectors
        ### create a numpy array of zeroes the size of m for weight, w
        #m = len(self.vocabulary)

        yHat = 0
        yStar = 0

        for fortune in self.featureVectorList:
            ### yHat and yStar are in the set {+1, -1}

            yStar = sign(int(fortune[0]))
            yHat = sign(self.w.dot(fortune[1]) )
            ### if the prediction doesn't match the label,
            ### update the weight
            if yHat != yStar:
                self.w = self.w + (self.eta * yStar * np.array(fortune[1]) )

        #print self.w

    ### end perceptron

    ### Check accuracy:
    def checkAccuracy (self):
        error = 0
        for fortune in self.featureVectorList:
            ### yHat and yStar are in the set {+1, -1}

            yStar = sign(int(fortune[0]))
            yHat = sign(self.w.dot(fortune[1]) )
            ### if the prediction doesn't match the label,
            ### update the weight
            if yHat != yStar:
                error += 1

        return error

    ### end checkAccuracy function

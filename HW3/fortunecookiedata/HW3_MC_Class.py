########################
### Marcus Blaisdell
### Cpt_S 315
### Homework #3
###
### HW3_MC_Class.py
###
########################

import numpy as np
from HW3_Functions import sign

class OCR ():
    featureVectorList = []
    labelListDict = {}
    labelList = []
    weightVectors = []
    eta = 1

    def __init__(self):
        pass

    ### end __init__ functions
    def readData(self, fileName):
        string = ''

        inFile = open (fileName, "r")

        string = inFile.readline()
        while string:
            index = 0
            featureVector = [0] * 128
            label = ''
            featureTuple = []

            ### if the line size is less than the size of a feature vector,
            ### it cannot contain a feature vector, so skip it:
            if len(string) < 128:
                pass
            else:
                ### move to the beginning of the data, it comes after the 'im' string
                while string[index] != 'i' and string[index + 1] != 'm':
                    index += 1

                ### move index to after the 'im' string
                index += 2

                ### populate the featureVector
                for x in range(index, index + 128):
                    featureVector[x - index] = string[x]

                ### get the feature label:
                label = string[index + 129]

                ### package the data in a list:
                featureTuple = [label, featureVector]

                ### add the feature vector to the feature vector list:
                self.featureVectorList.append (featureTuple)

            string = inFile.readline()

    ### end readData

    def buildLabelList(self):
        ### read through each feature vector and read the label:
        ### add unique labels to a dictionary:
        for element in self.featureVectorList:
            if self.labelListDict.get(element[0], '-') == '-':
                self.labelListDict[element[0]] = 1

        ### create a list of the unique labels:
        self.labelList = self.labelListDict.keys()

        ### sort the list alphabetically
        self.labelList.sort()

    ### end buildLabelList function

    def buildWeightVectors(self):
        for label in self.labelList:
            w = np.zeros(128, dtype=int)
            self.weightVectors.append(w)

    ### end buildWeightVectors function

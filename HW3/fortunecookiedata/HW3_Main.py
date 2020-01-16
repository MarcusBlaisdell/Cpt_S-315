########################
### Marcus Blaisdell
### Cpt_S 315
### Homework #3
###
### HW3_Main.py
###
########################

from HW3_FC_Class import *
from HW3_MC_Class import *
from HW3_Functions import *


myMC = OCR()

myMC.readData ("OCRdata/ocr_train.txt")
myMC.buildLabelList ()
myMC.buildWeightVectors ()


'''
### create an instance of our class:
myFC = FCookie()

### read data from text files:
myFC.readStops ("fortunecookiedata/stoplist.txt")
myFC.readLines ("fortunecookiedata/traindata.txt", myFC.trainData)
myFC.readLabels ("fortunecookiedata/trainlabels.txt")
myFC.readLines ("fortunecookiedata/testdata.txt", myFC.testData)
myFC.readLabels ("fortunecookiedata/testlabels.txt")

### create a vocabulary
myFC.vocabulary = buildVocabulary (myFC.trainData, myFC.stopList)

### create a feature vector list
myFC.featureVectorList = buildFeatureList (myFC.vocabulary, myFC.trainData, myFC.trainLabel)

### test Fortune Cookie classifier, 20 iterations

myFC.initializeWeight ()

for iteration in range (20):
    myFC.featureVectorList = buildFeatureList (myFC.vocabulary, myFC.trainData, myFC.trainLabel)

    myFC.perceptron ()

    trainError = myFC.checkAccuracy()

    myFC.featureVectorList = buildFeatureList (myFC.vocabulary, myFC.testData, myFC.trainLabel)

    testError = myFC.checkAccuracy()

    print 'Iteration: ', iteration + 1, ' : Training Errors = ', trainError, ' : Testing Errors = ', testError

print myFC.w

### end test Fortune Coookie Classifier
'''
'''
### for troubleshooting:
print len(myFC.stopList)
print len(myFC.trainData)
print len(myFC.trainLabel)
print len(myFC.vocabulary)
print len(myFC.featureVectorList)
'''

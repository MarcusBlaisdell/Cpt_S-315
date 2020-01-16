'''
Marcus Blaisdell
CptS 315
Homework #1
2/8/18
Professor Jana Doppa

HW1_Main.py

This file is the main program
'''

from HW1_Prep import *

support = 100

### format textfile to a python list:

inputList = getList ()

### create an indexable table of unique items from
### baskets in inputList:

uniqueItems = createTableOne(inputList)

### count items:

uniqueCount = pass1(inputList, uniqueItems)

### get a list of indexes that have counts
### greater-than-equal-to the support level

frequentItems = filter1(uniqueCount, support)

#pairs = genPairs(frequentItems)
#print("pairs complete")
pairs2 = pass2(inputList, uniqueItems, uniqueCount, support, frequentItems)
print ("pairs2 complete")
pairs = countPairs(pairs2)
print ("count pairs complete")

#triples = genTriples(frequentItems)
#print ("triples complete")
triples2 = pass3(inputList, uniqueItems, uniqueCount, support, frequentItems)
print ("triples2 complete")
triples = countTriples(triples2)
print ("count triples complete")

pairScoresXY =  calcConfidencesXY (uniqueCount, pairs, len(inputList), uniqueItems)
pairScoresYX =  calcConfidencesYX (uniqueCount, pairs, len(inputList), uniqueItems)

tripleScoreXYZ = calcConfidencesXYZ (uniqueCount, triples, len(inputList), uniqueItems)
tripleScoreXZY = calcConfidencesXZY (uniqueCount, triples, len(inputList), uniqueItems)
tripleScoreYZX = calcConfidencesYZX (uniqueCount, triples, len(inputList), uniqueItems)

mergeSort(pairScoresXY)
mergeSort(pairScoresYX)
mergeSort(tripleScoreXYZ)
mergeSort(tripleScoreXZY)
mergeSort(tripleScoreYZX)

outFile = open('output.txt', 'w')

outFile.write ('OUTPUT A: ')
outFile.write ('\n')

for x in range (5):
    outFile.write (pairScoresXY[x][0][0])
    outFile.write (' ')
    outFile.write (pairScoresXY[x][0][0])
    outFile.write (' ')
    outFile.write (str(pairScoresXY[x][1]))
    outFile.write ('\n')

for x in range (5):
    outFile.write (pairScoresYX[x][0][0])
    outFile.write (' ')
    outFile.write (pairScoresYX[x][0][0])
    outFile.write (' ')
    outFile.write (str(pairScoresYX[x][1]))
    outFile.write ('\n')

outFile.write ('OUTPUT B: ')
outFile.write ('\n')

for x in range (5):
    outFile.write (tripleScoreXYZ[x][0][0])
    outFile.write (' ')
    outFile.write (tripleScoreXYZ[x][0][0])
    outFile.write (' ')
    outFile.write (str(tripleScoreXYZ[x][1]))
    outFile.write ('\n')

for x in range (5):
    outFile.write (tripleScoreXZY[x][0][0])
    outFile.write (' ')
    outFile.write (tripleScoreXZY[x][0][0])
    outFile.write (' ')
    outFile.write (str(tripleScoreXZY[x][1]))
    outFile.write ('\n')

for x in range (5):
    outFile.write (tripleScoreYZX[x][0][0])
    outFile.write (' ')
    outFile.write (tripleScoreYZX[x][0][0])
    outFile.write (' ')
    outFile.write (str(tripleScoreYZX[x][1]))
    outFile.write ('\n')

outFile.close()

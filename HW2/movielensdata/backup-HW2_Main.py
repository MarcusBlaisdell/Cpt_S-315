'''
Marcus Blaisdell
CptS 315
Homework #2
2/28/18
Professor Jana Doppa

HW2_Main.py

This file is the main program
'''

###
import json
from HW2_Functions import *
from math import *

movieDict = {}
scores = {}
score = 0.0
userList = []
pairList = []
maxUserId = 671

userList = readRatings()
movieDict = readMovies(userList, userList[len(userList) - 1][0])
movieList = makeMovieList()

### uncomment this block to read scores from file instead of
### re-calculating
'''
### read scoreList from file
scoreList = {}
scoreList = readScoresFromFile()
print scoreList
### end read scoreList from file
'''

scoreList = {}
scoreList = scoreMovies(movieDict)

### calculate recommendations
userDict = estimateRatings(userList, scoreList, movieDict, userList[len(userList) - 1][0])

### print recommendations to a nicely formatted text file:
printRecommendations(userDict, movieList)

### save results to text files:

outFile = open ("output.txt", "w")
for x in userDict.keys():
    outFile.write ('User-id')
    outFile.write (str(x))
    outFile.write (' ')
    for y in range (5):
        outFile.write ('movie-id')
        outFile.write (str(userDict.get(x)[y][0]))
        outFile.write (' ')
    outFile.write ('\n')
outFile.close ()

### This one is easier to read for humans

outFile = open ("formattedRecommendations.txt", "w")
for x in userDict.keys():
    outFile.write (str(x))
    outFile.write ('\n')
    outFile.write (str(userDict.get(x)))
    outFile.write ('\n')
outFile.close()

### These are easier to rebuild for the computer
outFile = open("recommendations.txt", "w")
outFile.write(json.dumps(userDict))
outFile.close()

outFile = open("reloadoutput.txt", "w")
outFile.write(json.dumps(scoreList))
outFile.close()

### uncomment to read in from file
'''
inFile = open("reloadoutput.txt", "r")
data = json.loads(inFile.read())
inFile.close()
### test if successful:
print 'data'
print data['45440']
'''

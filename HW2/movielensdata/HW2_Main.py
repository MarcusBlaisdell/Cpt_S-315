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
print ("User List loaded")
movieDict = readMovies(userList, userList[len(userList) - 1][0])
print ("movie dictionary created")
movieList = makeMovieList()
print ("movie list created")

### uncomment this block to read scores from file instead of
### re-calculating
'''
### read scoreList from file
scoreList = {}
scoreList = readScoresFromFile()
print scoreList
### end read scoreList from file
'''

### scoreList contains a list of each movie
### and the top 5 similar movies by score :

scoreList = {}
scoreList = scoreMovies(movieDict)
print ("score list created")

### calculate recommendations
userDict = estimateRatings(userList, scoreList, movieDict, userList[len(userList) - 1][0])
print ("ratings dictionary created")

### print recommendations to a nicely formatted text file:
printRecommendations(userDict, movieList)

### save results to text files:

printOutput(userDict)

### print *Done* message to user:

print ' '
print '*** Complete ***'
print ' '

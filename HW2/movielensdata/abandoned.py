'''
def readRatings():

    inFile = open("ratings.csv", "r")

    string = inFile.readline()
    word = ""
    index = 0
    userIdMax = 0
    userList = []
    line = []

    while string:
        for x in string:
            if x == '\n':
                userList.append(line)
                line = []
                word = ""
            if x != ',':
                word += x
            else:
                if index == 0:
                    try:
                        word = int(word)
                        if word > userIdMax:
                            userIdMax = word
                    except:
                        pass

                line.append(word)

                index += 1

                word = ""
        index = 0

        string = inFile.readline()

    inFile.close()

    ### build an item (movies) matrix:

    inFile = open("movies.csv", "r")

    string = inFile.readline()
    word = ""
    index = 0
    movieDict = {}

    while string:
        for x in string:
            if x != ',' and x != '\n':
                word += x
            else:
                if index == 0:
                    if movieDict.get(word, 'n') == 'n':
                        #theList = [0] * (max(userDict.keys () ) + 1)
                        theList = [0] * (userIdMax + 1)
                        movieDict[word] = theList
                        #print word
                    else:
                        pass
                index += 1
                #print word
                word = ""
        index = 0
        string = inFile.readline()


    #print movieDict.keys()
    #print movieDict.get ('8485')
    #print len(movieDict.get('8485'))

    inFile.close()

    ### read through each line in the ratings matrix and add ratings to the
    ### item matrix in the appropriate locations
    ### userId's are indexes
    ### userList[0] = userId
    ### userList[1] = movieID
    ### userList[2] = ratings

    for x in userList:
        try:
            movieDict[x[1]][x[0]] = x[2]
        except:
            pass

    return movieDict
'''

### create a list of x from ratings.csv
### This maxed out the hard drive!!!

def genPairs(userList):
    user = 0
    lastUser = 0
    movieList = []
    pairList = []
    outFile = open ("pairs.txt", "w")

    for x in range(len(userList)):
    #for x in range(3000):
        user = userList[x][0]
        if user == lastUser:
            movieList.append(userList[x][1])
            #print user, 'newMovieList', userList[x][1]
        else:
            lastUser = user
            for y in range(len(movieList) ):
                for z in range(y + 1, len(movieList) ):
                    pair = (movieList[y], movieList[z])
                    #pairList.append(pair)
                    outFile.write (str(pair) )
                    outFile.write ('\n')

    outFile.close ()
    return pairList
### end genPairs function

def estimateRatings(userList, scoreList, movieDict:
    userDict = {}
    movieList = movieDict.keys()
    curUser = 0
    #for x in userList:
        #print x[0]
    for movie in movieList:
        ### movie[0] is userId
        if movie[0] == curUser:
            #print userList[0]
            movieList.append (movie[1])
        else:
            userDict[curUser] = movieList
            curUser = movie[0]
            movieList = []

    userList = userDict.keys()
    for user in userList:
        movieList = userDict.get(user)
        for movie in movieList:
            if scoreList.get(movie, 'n') != 'n':
                pairList = scoreList.get(movie)
                for pair in pairList:
                    try:
                        movieList.index(pair[1])
                    except:
                        predScore = predictScore()

    return userDict

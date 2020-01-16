### read in ratings.csv into a matrix (list of lists)
### Determine the number of users from ratings.csv

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

#print movieDict.get('4')


inFile = open ("traindatatest.txt", "r")

trainData = []
lineList = []
word = ''

string = inFile.readline()
count = 0

while string:

    for letter in range (len(string) ):
    #for letter in string:
        #print '.', string[letter], '.'
        #print '.', letter, '.'
        if letter == len(string) - 1:
        #if letter == '\r':
            print 'here'
            lineList.append(word)
            trainData.append (lineList)
            lineList = []
            word = ''
        elif string[letter] == ' ':
        #elif letter == ' ':
            lineList.append(word)
            word = ''
        else:
            word += string[letter]
            #word += letter

    #print count, ' : ', lineList[count]
    print 'lineList: ', lineList
    print 'trainData: ', trainData
    count += 1

    string = inFile.readline()

inFile.close()

### end readLines

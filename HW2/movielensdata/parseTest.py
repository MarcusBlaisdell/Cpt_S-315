### read in from file to dictionary

inFile = open ("output.txt", "r")
string = inFile.readline()

line = []
word = ""
testDict = {}

while string:
    for x in string:
        if x == '\n':
            line.append(word)
            word = ""
            storeList = []
            #string = inFile.readline()
            pair1 = (line[1], line[2])
            score1 = line[3]
            pair2 = (line[4], line[5])
            score2 = line[6]
            pair3 = (line[7], line[8])
            score3 = line[9]
            pair4 = (line[10], line[11])
            score4 = line[12]
            pair5 = (line[13], line[14])
            score5 = line[15]
            list1 = [pair1, score1]
            list2 = [pair2, score2]
            list3 = [pair3, score3]
            list4 = [pair4, score4]
            list5 = [pair5, score5]
            storeList = [list1, list2, list3, list4, list5]
            testDict[line[0]] = storeList
            line = []

        elif x == ',':
            line.append(word)
            word = ""
        elif x != '(' and x != ')' and x!= '[' and x!= ']' and x!= '"':
            word += str(x)
        else:
            pass

    string = inFile.readline()

inFile.close()

print testDict

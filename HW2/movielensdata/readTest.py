
inFile = open ("movies.csv", "r")

movieList = []
line = []
string = inFile.readline()
word = ""

while string:
    for x in string:
        if x == '\n':
            line.append(word)
            movieList.append(line)
            line = []
            word = ""
        elif x == ',':
            line.append(word)
            word = ""
        else:
            word += x

    string = inFile.readline()

inFile.close()

for x in movieList:
    print x[0], ' : ', x[1]

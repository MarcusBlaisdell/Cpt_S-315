import json

inFile = open ("backup-recommendations.txt", "r")
userDict = json.loads(inFile.read())
inFile.close()

outFile = open ("Testoutput.txt", "w")
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

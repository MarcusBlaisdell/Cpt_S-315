'''
Marcus Blaisdell
CptS 315
Homework #1
2/8/18
Professor Jana Doppa

HW1_Apriori.py
This file contains the execution of the A-priori algorithm
'''

### Python 3.6

DEBUG = 1

### Open input file for reading:

myFile = open("browsingdata.txt", "r")

### read the first line to get started

myStr = myFile.readline()

### Declare the variables that will be used in the loop:
### inputList is the master list that will hold the individual lists
### lineList is the individual lists
### newStr is the new string that is generated as text is read character-by
### character from each line and parsed into separate strings to be added
### to the lineList

inputList = []
lineList = []
newStr = ""

### Read until input is no longer valid:

while myStr:
    for x in myStr:
        if x != ' ':
            if x != '\n':
                newStr += x
        else:
            lineList.append(newStr)
            newStr = ""
    inputList.append(lineList)
    lineList = []
    myStr = myFile.readline()

### first pass:
### read each string from each list,
### if the string has been encountered before, increment its count,
### if it has not yet been encountered, add it to our matrix (python dictionary)
### and set its count to 1

### each x in inputList is a basket of items:
### each y in x is an item in a basket

table1Dict = {}

for x in inputList:
    for y in x:
        if (table1Dict.get(y, 0) == 0):
            table1Dict[y] = 1
        else:
            table1Dict[y] += 1

#####################################################
### test dictionary:
if DEBUG == 1:
    outFile = open("outFile.txt", "w")
    for x in table1Dict.keys():
        outFile.write (x)
        outFile.write (" : ")
        outFile.write (str (table1Dict.get(x)))
        outFile.write ('\n')

    outFile.close()
### end test dictionary
#####################################################
 
myFile.close()

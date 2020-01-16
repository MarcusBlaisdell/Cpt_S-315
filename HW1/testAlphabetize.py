theList = [[['FRO40251', 'DAI93865'], 1.0]]
theList.append ( [['FRO40251', 'GRO85051'], 0.9991694352159468] )
theList.append ([['FRO40251', 'GRO38636'], 0.9903846153846154] )
theList.append ([['FRO40251', 'ELE12951'], 0.9903846153846154] )
theList.append ([['FRO40251', 'DAI88079'], 0.986013986013986] )

for element in theList:
    print (element)

#def fixOrder (theList):
for index in range(4):
    cell = 0
    pos = 0
    i = 0

    if theList[index][1] == theList[index + 1][1]:
        while theList[index][0][pos][i] <= theList[index + 1][0][pos][i] and pos < len(theList[index][0]):
            if i < len(theList[index][0][pos]) - 1:
                i += 1
            else:
                i = 0
                pos += 1
        if pos < len(theList[index][0]):
            swap = theList[index]
            theList[index] = theList[index + 1]
            theList[index + 1] = swap

print ("After:")
for element in theList:
    print (element)

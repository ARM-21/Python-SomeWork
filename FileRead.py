
def fileReader(filePath='rent_details.txt'):
    """(This method reads the given file path and returns the values in list containing each element as dictionary.)\n
    argument---> str\n
    returns---> list
    """
    newDict = {}
    updatedList = []
    mainFile = open(filePath)
    dataInList = mainFile.readlines()
    listForKey = dataInList[0].strip().split(',');
    listForKey = ["Kitta","Location","Direction(land)","Anna","Price(per/month)","Availability"]
    for i in range(len(dataInList)):
        valueForDict = [];
        valueForDict = dataInList[i].strip().split(',');
        newDict = newDict.fromkeys(listForKey);
        for j in range(len(valueForDict)):
            newDict[listForKey[j]] = valueForDict[j]
        updatedList.append(newDict)
    mainFile.close()
    return updatedList;   
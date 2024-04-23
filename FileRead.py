def fileReader(filePath='rent_details.txt'):
    """(This method reads the given file path and returns the values in list containing each element as dictionary.)\n
    argument---> str\n
    returns---> list
    """
    newDict = {}
    updatedList = []
    mainFile = open(filePath)
    dataInList = mainFile.readlines()
    # print(dataInList);
    listForKey = dataInList[0].strip().split(',');
    listForKey = ["Kitta","Location","Direction(land)","Anna","Price(per/month)","Availability"]
    
    # print(listForKey);
    for i in range(len(dataInList)):
        valueForDict = [];
        # if i == 0:
        #     continue
        # print(valueForDict);
        valueForDict = dataInList[i].strip().split(',');
        # print(valueForDict)
        newDict = newDict.fromkeys(listForKey);
        for j in range(len(valueForDict)):
            # print(j)
            newDict[listForKey[j]] = valueForDict[j]
        updatedList.append(newDict)
    # print(newDict)
    # print(updatedList)
    mainFile.close()
    return updatedList;

# print(fileReader());    
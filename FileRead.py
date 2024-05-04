
def fileReader(filePath='rent_details.txt'):
    """(This method reads the given file path and returns the values in list containing each element as dictionary.)\n
    argument---> str\n
    returns---> list
    """
    # Initialization:
    newDict = {}  # Create an empty dictionary
    # using a list datatype to hold all the details form rent_details.txt file
    updatedList = []   # Initialize an empty list for dictionaries
    mainFile = open(filePath)   #Opening the File:
    dataInList = mainFile.readlines()  # Read lines from the file
    # example for list to store keys 
    listForKey = ["Kitta","Location","Direction(land)","Anna","Price(per/month)","Availability"] #for keys in dictionary

    for i in range(len(dataInList)):
        valueForDict = []
        valueForDict = dataInList[i].strip().split(',')   # Split line into values
        newDict = newDict.fromkeys(listForKey)   # Create a dictionary with keys
        for j in range(len(valueForDict)):
            newDict[listForKey[j]] = valueForDict[j]   # Assign values to keys in the dictionary
        updatedList.append(newDict) # Add dictionary to the list
    mainFile.close()  # Close the file
    return updatedList;     # Return the list of dictionaries


str = "man neupane1"
print(str.isalpha())
arr = str.split()
for value in arr:
    print(value.isalpha())
# print(arr)
# print(arr[[i for i in range(len(arr))]].isalpha())
# print((arr[0]+arr[1]).isdigit())
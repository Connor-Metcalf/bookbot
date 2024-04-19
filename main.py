# auxillary functions ----------------------------------------------------------

def createDictOfRepeatChar(text):
    repeatLettersDict = {}
    text = text.lower()

    for element in text:
        if element.isalpha():
            repeatLettersDict[element] = repeatLettersDict.get(element, 0) + 1

    return repeatLettersDict        

def createListOfDictsFromDict(dictionary):
    newList = []

    for k, v in dictionary.items():
        newDictElement = dict( [ ('letter', k), ('repeats', v) ] )
        newList.append(newDictElement)

    return newList

def getBookText(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    wordArray = text.split()
    return len(wordArray)

def printFormattedList(list):
    for element in list:
        print(f"The '{element['letter']}' character was found "
              f"{element['repeats']} times")

def sortListofDicts(list):
    list.sort(reverse = True, key = lambda dict: dict['repeats'] )
    return list

# main program------------------------------------------------------------------

def main():
    # create and populate variables
    book_path = "books/frankenstein.txt"

    text = getBookText(book_path)

    numWords = getWordCount(text)

    repeatLettersDict = createDictOfRepeatChar(text)

    repeatsList = createListOfDictsFromDict(repeatLettersDict)
    repeatsList = sortListofDicts(repeatsList)

    print(f"\nInput file '{book_path}' received.\n\nRunning analysis. . .\n")

    print(f"Number of words in text: {numWords}\n")

    printFormattedList(repeatsList)
     
    # end of program
    print("\n                       . . . Analysis complete.\n\nEnd of program")
    
# run program ------------------------------------------------------------------
main()    

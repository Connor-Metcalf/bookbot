# main function ----------------------------------------------------------------

def main():
    # create and populate variables
    book_path = "books/frankenstein.txt"

    text = getBookText(book_path)
    numWords = getWordCount(text)
    repeatLetters = createDictOfRepeatChar(text)
    repeatLetters = sortDictionary(repeatLetters)
    
    print("\nRunning analysis. . .\n\n")

    print(f"Number of words in text: {numWords}\n\n")

    print(f"Repeat characters in text: {repeatLetters}\n\n")
    
    # end of program
    print("Analysis complete.\n\nEnd of program")
    
    
# auxillary functions ----------------------------------------------------------

def getBookText(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    wordArray = text.split()
    return len(wordArray)

def createDictOfRepeatChar(text):
    repeatLettersDict = {}
    text = text.lower()

    for element in text:
        repeatLettersDict[element] = repeatLettersDict.get(element, 0) + 1

    return repeatLettersDict        

def sortDictionary(dictionary):
    keys = list( dictionary.keys() )
    keys.sort()
    dictionary = {index: dictionary[index] for index in keys}

    return dictionary
        
# run program ------------------------------------------------------------------
main()    

# main function ----------------------------------------------------------------

def main():
    # create and populate variables
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)
    numWords = getWordCount(text)
    
    # display variables
    print(f"{numWords} words found in document.\n")

    # end of program
    printInAllLowerCase("END OF PROGRAM")
    
    
# auxillary functions ----------------------------------------------------------

def getBookText(path):
    with open(path) as f:
        return f.read()

def getWordCount(text):
    wordArray = text.split()
    return len(wordArray)

def printInAllLowerCase(text):
    text = text.lower()
    print(text)

def printDictOfRepeatChar(text):
    repeatLettersDict = {}
    
        
# run program ------------------------------------------------------------------
main()    

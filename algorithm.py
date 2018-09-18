#input: array of 5 words, max of 5 letters
words = ['dog', 'cat', 'chimp', 'eagle', 'snake']

#output: 2-dimensional matrix, 10x10, where the words are displayed horizontally or vertically (NO DIAGONAL)
# Example output:
filledArray = [
    ['a', "d", "o", "g", 'f', 'q', "e", 'm', 'a', 'o'],
    ['r', 'h', 'a', 'g', 'f', 'q', "a", 'l', 'h', 'p'],
    ['s', 'l', 'y', 'o', 'f', 'q', "g", 'e', 'u', 'v'],
    ['p', 'i', 'a', 'g', 'f', 'q', "l", 't', 'u', 'b'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['' for i in range(10)],
    ['' for i in range(10)],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
]


# Approach:
# 1. loop through words array, looking at one word at a time (i.e. 'dog')
# 2. randomly select horizontal or vertical (50-50 chance)
# 3. if horizontal, run horizontal function:
#     - randomly select which row (index 0-9)
#     - randomly select which column to start at (index 0-9)
#     - randomly select forward or backward reading (50-50 chance)
#     - if its forward, check to make sure that it is not too close to the right side
#         10 - columnIndex must be greater than or equal to word length, or else reassign to read backwards)
#     - if its backward, check to make sure that it is not too close to the left side
#         columnIndex + 1 must be greater than or equal to word length, or else rassign to read forwards
#     - iterate through result array according to length of word to make sure that there are enough blank spaces
#         if not enough blank spaces, choose a new row index and new column index
#     - assuming there are enough blank spaces, reassign the values of the array template
#         resultsArray[rowIndex][columnIndex +/- counter] = letter, for each letter in the word
# 4. if vertical, run vertical function:
#     ////stuff will go here
# 5. at end, return the results array



import random

wordSearchTemplate = [['' for i in range(10)] for i in range(10)]


def horizontalAssign(word, resultsArray):
    rowIndex = random.randint(0, 9)
    forward = random.randint(0, 1)
    if(forward):
        # makes sure you're not too close to the right side
        columnIndex = random.randint(0, 10 - len(word))

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < len(word):
            if(rowSwitches == 10 and columnSwitches == (11 - len(word))):
                # no where for the word to fit
                return False
            elif rowSwitches == 10:
                # no rows available for that column index, so switch columns
                rowSwitches = 0
                columnIndex = (columnIndex - 1) % (11 - len(word))
                columnSwitches += 1

            checkValue = resultsArray[rowIndex][columnIndex + i]
            if checkValue == '':
                i += 1
            else:
                # if the spots are already taken, check the next row
                rowIndex = (rowIndex + 1) % 10
                rowSwitches += 1
                i = 0

        #should have correct rowIndex, colIndex by this point
        for j in range(len(word)):
            resultsArray[rowIndex][columnIndex + j] = word[j]
        
    
    else:
        # make sure you're not too close to the left side
        columnIndex = random.randint(len(word) - 1, 9)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < len(word):
            if(rowSwitches == 10 and columnSwitches == (11 - len(word))):
                # no where for the word to fit
                return False
            elif rowSwitches == 10:
                # no rows available for that column index, so try next column
                rowSwitches = 0
                columnIndex = columnIndex + 1
                if columnIndex == 10:
                    columnIndex = len(word) - 1
                columnSwitches += 1

            checkValue = resultsArray[rowIndex][columnIndex - i]
            if checkValue == '':
                i += 1
            else:
                # if the spots are already taken, check the next row
                rowIndex = (rowIndex + 1) % 10
                rowSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j in range(len(word)):
            resultsArray[rowIndex][columnIndex - j] = word[j]
    
    return resultsArray


def verticalAssign(word, resultsArray):
    columnIndex = random.randint(0, 9)
    readDownwards = random.randint(0, 1)
    if(readDownwards):
        # makes sure you're not too close to the bottom
        rowIndex = random.randint(0, 10 - len(word))

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < len(word):
            if(columnSwitches == 10 and rowSwitches == (11 - len(word))):
                # nowhere for the word to fit
                return False
            elif columnSwitches == 10:
                # no columns available for that row index, so switch rows
                columnSwitches = 0
                rowIndex = (rowIndex + 1) % (11 - len(word))
                rowSwitches += 1

            checkValue = resultsArray[rowIndex + i][columnIndex]
            if checkValue == '':
                i += 1
            else:
                # if the spots are already taken, check the next column
                columnIndex = (columnIndex + 1) % 10
                columnSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j in range(len(word)):
            resultsArray[rowIndex + j][columnIndex] = word[j]
    
    else:
        # make sure you're not too close to the top
        rowIndex = random.randint(len(word) - 1, 9)

        i = 0
        rowSwitches = 0
        columnSwitches = 0
        while i < len(word):
            if(columnSwitches == 10 and rowSwitches == (11 - len(word))):
                # no where for the word to fit
                return False
            elif columnSwitches == 10:
                # no rows available for that column index, so try next column
                columnSwitches = 0
                rowIndex = rowIndex + 1
                if rowIndex == 10:
                    rowIndex = len(word) - 1
                rowSwitches += 1

            checkValue = resultsArray[rowIndex - i][columnIndex]
            if checkValue == '':
                i += 1
            else:
                # if the spots are already taken, check the next row
                columnIndex = (columnIndex + 1) % 10
                columnSwitches += 1
                i = 0

        #should have correct rowIndex and columnIndex by this point
        for j in range(len(word)):
            resultsArray[rowIndex - j][columnIndex] = word[j]
    
    return resultsArray

matrix = verticalAssign('chimp', wordSearchTemplate)
for i in range(10):
    print matrix[i]


def generateCrossword(wordList):
    resultMatrix = [['' for i in range(10)] for i in range(10)]
    for i in range(len(wordList)):
        horizontalAssign(wordList[i], resultMatrix)
    return resultMatrix


# result = generateCrossword(['dog', 'cat', 'pizza', 'carl', 'chimp'])
# for i in range(10):
#     print result[i]
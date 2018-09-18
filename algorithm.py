#INPUT: List of words
# (words longer than 5 letters increase the chance that a word-search cannot mathematically be created)
words = ['dog', 'cat', 'chimp', 'eagle', 'snake']

#output: 2-dimensional matrix, 10x10, where the words are displayed horizontally or vertically (NO DIAGONAL)
# Example output:
filledArray = [
    ['a', "d", "o", "g", 'f', 'q', "e", 'm', 'a', 'o'],
    ['r', 'h', 'a', 'g', 'f', 'q', "a", 'l', 'h', 'p'],
    ['s', 'l', 'y', 'o', 'f', 'q', "g", 'e', 'u', 'v'],
    ['p', 'i', 'a', 'g', 'f', 'q', "l", 't', 'u', 'b'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['' for i in range(10)], #row not filled for testing purposes
    ['' for i in range(10)], #row not filled for testing purposes
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
    ['i', 'd', 'p', 'e', 'f', 'q', "e", 'q', 'a', 'e'],
]


# Approach:
# 1. loop through words array, looking at one word at a time (i.e. 'dog')
# 2. randomly select horizontal, vertical, or diagonal (random number 1-3)
# 3. if horizontal, run horizontal function:
#   - if it returns False, try running the vertical function on that word instead
# 4. if vertical, run vertical function:
#   - if it returns False, try running the diagonal function on that word instead
# 5. if diagonal, run the diagonal function:
#   - if it returns False, try running the horizontal function
# 6. keep counter to ensure that it only tries each method once for each word
#   - return False if each direction has been tried with no luck
# 7. after each word has been inserted, loop through results Array, replacing '' with random letter
# 8. return the results Array





import random
import string
alphabet = string.letters[0:26]

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








def diagonalAssign(word, resultsArray):
    directionIndicator = random.randint(1, 4)

    if directionIndicator == 1:
        #reads top-to-bottom, left-to-right \
        rowIndex = random.randint(0, 10 - len(word))
        columnIndex = random.randint(0, 10 - len(word))

        i = 0
        columnSwitch = 0
        rowSwitch = 0
        while(i < len(word)):
            if(columnSwitch == 11 - len(word) and rowSwitch == 11 - len(word)):
                return False
            if(columnSwitch == 11 - len(word)):
                columnSwitch = 0
                rowIndex = (rowIndex + 1) % (11 - len(word))
                rowSwitch += 1

            checkValue = resultsArray[rowIndex + i][columnIndex + i]
            if checkValue == '':
                i += 1
            else:
                columnIndex = (columnIndex + 1) % (11 - len(word))
                columnSwitch += 1
                i = 0

        for j in range(len(word)):
            resultsArray[rowIndex + j][columnIndex + j] = word[j]

    elif directionIndicator == 2:
        #reads top-to-bottom, right-to-left /
        rowIndex = random.randint(0, 10 - len(word))
        columnIndex = random.randint(len(word) - 1, 9)

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < len(word):
            if(rowsChecked == 11 - len(word) and columnsChecked == 11 - len(word)):
                return False
            elif(rowsChecked == 11 - len(word)):
                rowsChecked = 0
                columnIndex = columnIndex + 1
                if columnIndex > len(resultsArray) - 1:
                    columnIndex = len(word) - 1
                columnsChecked += 1

            checkValue = resultsArray[rowIndex + i][columnIndex - i]
            if checkValue == '':
                i += 1
            else:
                rowIndex = (rowIndex + 1) % (11 - len(word))
                rowsChecked += 1
                i = 0
        
        for j in range(len(word)):
            resultsArray[rowIndex + j][columnIndex - j] = word[j]

    elif directionIndicator == 3:
        #reads bottom-to-top, right-to-left \
        rowIndex = random.randint(len(word) - 1, 9)
        columnIndex = random.randint(len(word) - 1, 9)

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < len(word):
            if(rowsChecked == 11 - len(word) and columnsChecked == 11 - len(word)):
                return False
            elif(rowsChecked == 11 - len(word)):
                rowsChecked = 0
                columnIndex = columnIndex + 1
                if columnIndex > 9:
                    columnIndex = len(word) - 1
                columnsChecked += 1

            checkValue = resultsArray[rowIndex - i][columnIndex - i]
            if checkValue == '':
                i += 1
            else:
                rowIndex += 1
                if rowIndex > 9:
                    rowIndex = len(word) - 1
                rowsChecked += 1
                i = 0
        
        for j in range(len(word)):
            resultsArray[rowIndex - j][columnIndex - j] = word[j]

    else:
        #reads bottom-to-top, left-to-right /
        rowIndex = random.randint(len(word) - 1, 9)
        columnIndex = random.randint(0, 10 - len(word))

        i = 0
        rowsChecked = 0
        columnsChecked = 0
        while i < len(word):
            if(rowsChecked == 11 - len(word) and columnsChecked == 11 - len(word)):
                return False
            elif(rowsChecked == 11 - len(word)):
                rowsChecked = 0
                columnIndex = (columnIndex + 1) % (11 - len(word))
                columnsChecked += 1

            checkValue = resultsArray[rowIndex - i][columnIndex + i]
            if checkValue == '':
                i += 1
            else:
                rowIndex += 1
                if rowIndex > 9:
                    rowIndex = len(word) - 1
                rowsChecked += 1
                i = 0
        
        for j in range(len(word)):
            resultsArray[rowIndex - j][columnIndex + j] = word[j]

    return resultsArray








def generateWordSearchEasy(wordList):
    resultMatrix = [['' for i in range(10)] for i in range(10)]
    for i in range(len(wordList)):
        direction = random.randint(1,2)
        if direction == 1:
            horizontalAssign(wordList[i], resultMatrix)
        else:
            verticalAssign(wordList[i], resultMatrix)

    for i in range(len(resultMatrix)):
        for j in range(len(resultMatrix[i])):
            if resultMatrix[i][j] == '':
                resultMatrix[i][j] = alphabet[random.randint(0, 25)]
    return resultMatrix




def generateWordSearchHard(wordList):
    resultMatrix = [['' for i in range(10)] for i in range(10)]

    for i in range(len(wordList)):
        direction = random.randint(1,3)

        impossible = True
        attempts = 0
        while attempts < 4 :
            if direction == 1:
                if horizontalAssign(wordList[i], resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 2
            elif direction == 2:
                if verticalAssign(wordList[i], resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 3
            else:
                if diagonalAssign(wordList[i], resultMatrix):
                    impossible = False
                    break
                else:
                    attempts += 1
                    direction = 1
        if impossible:
            return False #means that the word could not be inserted in any direction, user can try again

    for i in range(len(resultMatrix)):
        for j in range(len(resultMatrix[i])):
            if resultMatrix[i][j] == '':
                resultMatrix[i][j] = alphabet[random.randint(0, 25)]
    return resultMatrix


# result = generateWordSearchEase(['chimp', 'harry', 'alfred', 'heart', 'dog', 'zzzzz'])
# for i in range(len(result)):
#     print result[i]
# ^^^^^ For checking the easy function ^^^^^


# result = generateWordSearchHard(['chimp', 'harry', 'alfred', 'heart', 'dog', 'zzzzz'])
# for i in range(len(result)):
#     print result[i]
# ^^^^^ For checking the hard function ^^^^^


# print generateWordSearchHard(['chimpanzee', 'harrypotte', 'alfredosau', 'heartthrob', 'dogandcats', 'zzzzzzzzzz'])
# ^^^^^ For checking the error case ^^^^^

import pprint


testPuzzle = [
    ['m', 'r', 'n', 'x', 'm', 'g', 'q', 'q', 'b', 'f', 'n', 'm', 'k', 'f', 'z'],
    ['q', 'h', 'c', 'p', 'n', 'p', 'o', 'y', 'u', 'o', 't', 'w', 'b', 'j', 'z'],
    ['b', 'g', 'g', 'b', 'e', 't', 'c', 'd', 'i', 'a', 'l', 'f', 'r', 'e', 'd'],
    ['y', 'v', 'a', 'y', 'b', 'c', 'a', 'k', 'f', 'y', 'd', 'v', 'u', 'q', 'g'],
    ['r', 'r', 'y', 'v', 'h', 'y', 'y', 'n', 'p', 'e', 'w', 'j', 'd', 'i', 'o'],
    ['j', 'w', 'r', 'i', 'r', 'u', 'i', 'w', 'b', 's', 'w', 'r', 'o', 'j', 's'],
    ['s', 'l', 'm', 'a', 'a', 'z', 'n', 'p', 'z', 'j', 'e', 'n', 'q', 'g', 'r'],
    ['t', 'p', 'o', 'r', 'h', 'v', 'd', 's', 'z', 'm', 'x', 'o', 'd', 'j', 'e'],
    ['y', 'r', 'w', 'q', 'u', 'b', 'k', 'h', 'u', 's', 'd', 'h', 'z', 'r', 'u'],
    ['c', 'u', 'a', 'q', 'g', 'g', 'q', 'c', 'b', 'q', 'q', 'm', 'a', 'a', 'l'],
    ['n', 'g', 't', 'e', 'a', 'f', 'j', 'm', 'p', 'r', 'u', 't', 'l', 'q', 'g'],
    ['u', 'z', 'a', 'u', 'h', 'y', 'i', 'c', 'z', 'o', 'q', 'm', 'v', 'h', 'l'],
    ['o', 'w', 'b', 'p', 'n', 'm', 'b', 'd', 'z', 'h', 's', 'y', 'q', 'b', 'z'],
    ['e', 'x', 'y', 'c', 't', 'v', 'h', 'j', 'i', 'e', 'y', 'd', 'j', 'i', 'w'],
    ['c', 'l', 'o', 'i', 'y', 'b', 'l', 'f', 'l', 'p', 'n', 'z', 'h', 'w', 'p']
 ]

wordsToFind = ['chimp', 'harry', 'alfred', 'heart', 'dog']




def checkAtIndex(row, col, word, puzzle):
    positions = []
    letterCount = 0
    #check horizontally (rightwards)
    while letterCount < len(word):
        if col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check horizontally (leftwards)
    while letterCount < len(word):
        if col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check vertically (downwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check vertically (upwards)
    while letterCount < len(word):
        if row - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (upwards, rightwards)
    while letterCount < len(word):
        if row - letterCount < 0 or col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (downwards, rightwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle) or col + letterCount == len(puzzle):
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col + letterCount] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col + letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (upwards, leftwards)
    while letterCount < len(word):
        if row - letterCount < 0 or col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row - letterCount][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row - letterCount, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    #check diagonally (downwards, leftwards)
    while letterCount < len(word):
        if row + letterCount == len(puzzle) or col - letterCount < 0:
            positions = []
            letterCount = 0
            break
        elif puzzle[row + letterCount][col - letterCount] == word[letterCount]:
            positions.append({'rowNum': row + letterCount, 'colNum': col - letterCount})
            letterCount += 1
        else:
            positions = []
            letterCount = 0
            break
    if len(positions) == len(word): return positions

    return False





def solver(word, puzzle):
    for r, row in enumerate(puzzle):
        for c, letter in enumerate(row):
            foundIt = False
            if letter == word[0]: 
                foundIt = checkAtIndex(r, c, word, puzzle)
            if foundIt != False: 
                return foundIt
    return False



for word in wordsToFind:
    pprint.pprint(solver(word, testPuzzle))


# Output: [{rowNum: ..., colNum:...}, {rowNum: ..., colNum:...}, ...]
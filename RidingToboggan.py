def countOfTreesEncounteredDuringTobogganRide(moveRight, moveDown, treePattern):
    treeCount = 0
    currentColumn = 0
    currentRow = 0
    treePatternWidth = len(treePattern[0])
    while currentRow < len(treePattern):
        if(treePattern[currentRow][currentColumn % treePatternWidth] == '#'):
            treeCount = treeCount+1
        currentRow = currentRow+moveDown
        currentColumn = currentColumn+moveRight
    return treeCount

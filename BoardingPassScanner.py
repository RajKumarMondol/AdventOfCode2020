import math


def findRowNumber(seatInstruction, minRow, maxRow):
    # print(seatInstruction, minRow, maxRow)
    if len(seatInstruction) == 0:
        return minRow
    elif seatInstruction[0] == "F":
        return findRowNumber(seatInstruction[1:], minRow, math.floor((minRow+maxRow)/2))
    else:
        return findRowNumber(seatInstruction[1:], math.ceil((minRow+maxRow)/2), maxRow)


def findColumnNumber(seatInstruction, minColumn, maxColumn):
    # print(seatInstruction, minColumn, maxColumn)
    if len(seatInstruction) == 0:
        return minColumn
    elif seatInstruction[0] == "L":
        return findColumnNumber(seatInstruction[1:], minColumn, math.floor((minColumn+maxColumn)/2))
    else:
        return findColumnNumber(seatInstruction[1:], math.ceil((minColumn+maxColumn)/2), maxColumn)


def findSeatId(seatInstruction):
    rowNumber = findRowNumber(seatInstruction[:7], 0, 127)
    columnNumber = findColumnNumber(seatInstruction[7:], 0, 7)
    return rowNumber*8+columnNumber


assert (357 == findSeatId("FBFBBFFRLR"))
assert (567 == findSeatId("BFFFBBFRRR"))
assert (119 == findSeatId("FFFBBBFRRR"))
assert (820 == findSeatId("BBFFBBFRLL"))


def findMaxSeatId(seatingInstructions):
    maxSeatId = 0
    for seatingInstruction in seatingInstructions:
        seatId = findSeatId(seatingInstruction)
        if seatId > maxSeatId:
            maxSeatId = seatId

    return maxSeatId


def findMissingSeatId(seatingInstructions):
    flightSeatOccupency = {}
    minSeatId = 1024
    maxSeatId = 0
    for seatingInstruction in seatingInstructions:
        seatId = findSeatId(seatingInstruction)
        flightSeatOccupency[seatId] = seatingInstruction
        if seatId > maxSeatId:
            maxSeatId = seatId
        if seatId < minSeatId:
            minSeatId = seatId

    for seatId in range(minSeatId, maxSeatId):
        if not seatId in flightSeatOccupency:
            return seatId
    return -1

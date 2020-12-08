accumulatorValue = 0
currentInstructionIndex = 0


def moveToNextInstruction():
    global currentInstructionIndex
    currentInstructionIndex = currentInstructionIndex+1


def jumpToNextInstruction(params):
    global currentInstructionIndex
    currentInstructionIndex = currentInstructionIndex+int(params[0])


def updateAccumulator(params):
    global accumulatorValue
    accumulatorValue = accumulatorValue+int(params[0])
    moveToNextInstruction()


def doNothing(ignore):
    moveToNextInstruction()


executeInstructions = {
    "nop": doNothing,
    "acc": updateAccumulator,
    "jmp": jumpToNextInstruction
}


def accumulatorValueAtBeginingOfLoop(bootInstructions):
    global currentInstructionIndex
    global accumulatorValue

    executedInstructionIndexes = set([currentInstructionIndex])
    while currentInstructionIndex < len(bootInstructions):
        instructionParts = bootInstructions[currentInstructionIndex].split()
        executeInstructions[instructionParts[0]](instructionParts[1:])

        if currentInstructionIndex in executedInstructionIndexes:
            break
        executedInstructionIndexes.add(currentInstructionIndex)

    return accumulatorValue


def repairTheProgramAndCheckIfRunning(changeAtPosition, changeToInstruction, bootInstructions):
    global currentInstructionIndex
    global accumulatorValue

    currentInstructionIndex = 0
    accumulatorValue = 0

    executedInstructionIndexes = set([currentInstructionIndex])
    while currentInstructionIndex < len(bootInstructions):
        instructionParts = bootInstructions[currentInstructionIndex].split()
        if changeAtPosition == currentInstructionIndex:
            executeInstructions[changeToInstruction](instructionParts[1:])
        else:
            executeInstructions[instructionParts[0]](instructionParts[1:])

        if currentInstructionIndex in executedInstructionIndexes:
            return False
        executedInstructionIndexes.add(currentInstructionIndex)

    return True


def accumulatorValueAfterRepair(bootInstructions):
    global currentInstructionIndex
    global accumulatorValue

    for bootInstructionIndex in range(len(bootInstructions)):
        bootInstruction = bootInstructions[bootInstructionIndex]
        if bootInstruction.startswith("nop"):
            repairedInstruction = "jmp"
        elif bootInstruction.startswith("jmp"):
            repairedInstruction = "nop"
        else:
            repairedInstruction = ""

        if repairedInstruction != "":
            if repairTheProgramAndCheckIfRunning(bootInstructionIndex, "nop",  bootInstructions):
                break

    return accumulatorValue

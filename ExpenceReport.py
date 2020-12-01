
def calculateMultiplicationOfTwoEntriesWithSumOf(targetSum, numbers):
    for index in range(len(numbers)):
        secondNumber = numbers[index]
        possibleThirdNumber = targetSum-secondNumber
        if (possibleThirdNumber in numbers[index:]):
            return secondNumber*possibleThirdNumber
    return 0


def calculateMultiplicationOfThreeEntriesWithSumOf(targetSum, numbers):
    for index in range(len(numbers)):
        firstNumber = numbers[index]
        multiplicationOfTwoNumbers = calculateMultiplicationOfTwoEntriesWithSumOf(targetSum-firstNumber, numbers[index:])
        if multiplicationOfTwoNumbers > 0:
            return firstNumber*multiplicationOfTwoNumbers
    return 0

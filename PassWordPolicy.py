import re


def exactlyOneCharacterPasswordPolicy(positionOne, positionTwo, character, passWord):
    if bool(passWord[positionOne-1] == character) != bool(passWord[positionTwo-1] == character):
        return True
    return False


def characterCountPasswordPolicy(minCount, maxCount, character, passWord):
    policyCharacterCount = passWord.count(character)
    if minCount <= policyCharacterCount and policyCharacterCount <= maxCount:
        return True
    return False


def countOfValidPassword(policyWithPasswords, checkIfValidPassWord):
    validPassWordCount = 0
    for policyWithPassword in policyWithPasswords:
        policyWithPasswordComponents = re.split('-| |:', policyWithPassword)
        if checkIfValidPassWord(int(policyWithPasswordComponents[0]),
                                int(policyWithPasswordComponents[1]),
                                policyWithPasswordComponents[2],
                                policyWithPasswordComponents[3]):
            validPassWordCount = validPassWordCount + 1
    return validPassWordCount

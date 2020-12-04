import re


def isValidBYR(byr):
    if byr == "":
        return False
    return 1920 <= int(byr) and int(byr) <= 2002


assert(isValidBYR("1920"))
assert(isValidBYR("2002"))
assert(not isValidBYR(""))
assert(not isValidBYR("1919"))
assert(not isValidBYR("2003"))


def isValidIYR(iyr):
    if iyr == "":
        return False
    return 2010 <= int(iyr) and int(iyr) <= 2020


assert(isValidIYR("2010"))
assert(isValidIYR("2020"))
assert(not isValidIYR(""))
assert(not isValidIYR("2009"))
assert(not isValidIYR("2021"))


def isValidEYR(eyr):
    if eyr == "":
        return False
    return 2020 <= int(eyr) and int(eyr) <= 2030


assert(isValidEYR("2020"))
assert(isValidEYR("2030"))
assert(not isValidEYR(""))
assert(not isValidEYR("2019"))
assert(not isValidEYR("2031"))


def isValidHGT(hgt):
    if hgt.endswith("in"):
        inch = int(hgt[:-2])
        return 59 <= inch and inch <= 76
    elif hgt.endswith("cm"):
        cm = int(hgt[:-2])
        return 150 <= cm and cm <= 193
    return False


assert(isValidHGT("60in"))
assert(isValidHGT("190cm"))
assert(not isValidHGT(""))
assert(not isValidHGT("190in"))
assert(not isValidHGT("190"))

hclregex = re.compile("#[0-9a-f]{6}")


def isValidHCL(hcl):
    return hclregex.search(hcl)


assert(isValidHCL("#123abc"))
assert(not isValidHCL("#123abz"))
assert(not isValidHCL("123abc"))

assert(isValidHCL("#a97842"))
assert(isValidHCL("#88878f"))
assert(not isValidHCL(""))
assert(not isValidHCL("#60292"))


def isValidECL(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


assert(isValidECL("brn"))
assert(not isValidECL("wat"))

assert(isValidECL("amb"))
assert(isValidECL("oth"))
assert(not isValidECL(""))
assert(not isValidECL("xyz"))

pidregex = re.compile("^[0-9]{9}$")


def isValidPID(pid):
    return pidregex.search(pid)


assert(isValidPID("000000001"))
assert(not isValidPID("0123456789"))

assert(isValidPID("000000000"))
assert(isValidPID("123456789"))
assert(not isValidPID(""))
assert(not isValidPID("12345678"))
assert(not isValidPID("23456789"))

passportFieldValidations = {
    "byr": isValidBYR,
    "iyr": isValidIYR,
    "eyr": isValidEYR,
    "hgt": isValidHGT,
    "hcl": isValidHCL,
    "ecl": isValidECL,
    "pid": isValidPID
}


def checkForPassportFieldValueIgnoringCID(passport):
    for passportField in passportFieldValidations:
        if not passportField in passport:
            return False
        if not passportFieldValidations[passportField](passport[passportField]):
            return False
    return True


def checkForPassportFieldIgnoringCID(passport):
    for passportField in passportFieldValidations:
        if not passportField in passport:
            return False
    return True


def countValidPassport(passportBatchFile, passportValidator):
    allPassports = []
    passport = {}
    for passportBatchFileLine in passportBatchFile:
        if passportBatchFileLine == "" and len(passport) > 0:
            allPassports.append(passport)
            passport = {}
        else:
            fieldsWithValues = passportBatchFileLine.split()
            for fieldsWithValue in fieldsWithValues:
                fielsAndValue = fieldsWithValue.split(":")
                passport[fielsAndValue[0]] = fielsAndValue[1]
    if len(passport) > 0:
        allPassports.append(passport)

    # print(allPassports)
    # print(len(allPassports))

    validPassportCount = 0
    for passport in allPassports:
        if passportValidator(passport):
            validPassportCount = validPassportCount+1

    return validPassportCount

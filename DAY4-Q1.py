import json

def findValidPassports():

    f = open('day4-input.txt', 'r')

    # cid is optional field, all else are required.
    requiredPassportFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    validPassports = 0

    passportStringToDict = ''
    for line in f:
        if line == '\n':

            # Add beginning of dict
            passportString = '{'

            split = passportStringToDict.split()

            for i in split:
                key = i.split(':')[0]
                value = i.split(':')[1]
                key = '"' + key + '"'
                value = '"' + value + '"'

                newKeyValPair = key + ' : ' + value + ', '
                passportString += newKeyValPair

            # Remove last comma from string so can be converted to JSON
            passportString = passportString[:-2]

            # Add end of dict
            passportString += '}'

            # Convert string to dict
            passportDict = json.loads(passportString)
            print(passportDict)

            # Determine if passport is valid
            validPassportEntry = 0
            for field in requiredPassportFields:
                if field in passportDict.keys():
                    validPassportEntry += 1

            if validPassportEntry >= 7:
                validPassports += 1

            passportStringToDict = ''
            continue

        line = line.rstrip("\n")
        passportStringToDict += ' ' + line

    print(validPassports)

if __name__ == '__main__':
    findValidPassports()
    # 263 - no
    # 292 - no - too high
    # 294 - no
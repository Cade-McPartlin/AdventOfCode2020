import json

def findValidPassports():

    f = open('day4-input.txt', 'r')

    # cid is optional field, all else are required.
    requiredPassportFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    validPassports = 0

    passportStringToDict = ''
    for index, line in enumerate(f):
        print('index: ' + str(index))
        if line == '\n':
            line = line.rstrip("\n")
            passportStringToDict = passportStringToDict[1:]
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
            # print(passportDict)

            # Determine if passport is valid

            if all(x in passportDict for x in requiredPassportFields):
                print('VALID' + str(passportDict))
                print('KEYS: ' + str(passportDict.keys()))
                validPassports += 1

            # validPassportEntry = 0
            # for field in requiredPassportFields:
            #     if field in passportDict.keys():
            #         validPassportEntry += 1
            #
            # if validPassportEntry >= 7:
            #     validPassports += 1

            passportStringToDict = ''
            continue

        line = line.rstrip("\n")
        passportStringToDict += ' ' + line

    print('Valid Passports: ' + str(validPassports))

if __name__ == '__main__':
    findValidPassports()
    # 146 - no
    # 263 - no
    # 292 - no - too high
    # 294 - no
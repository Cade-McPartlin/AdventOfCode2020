import json
# https://adventofcode.com/2020/day/4
# Passport data is validated in batch files (your puzzle input).
# Each passport is represented as a sequence of key:value pairs
# separated by spaces or newlines. Passports are separated by blank lines.

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def findValidPassports():

    f = open('day4-input.txt', 'r')

    # cid is optional field, all else are required.
    requiredPassportFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    # total count of valid passports
    validPassports = 0

    passportStringToDict = ''
    for index, line in enumerate(f):

        # Passports are separated by empty lines
        if line == '\n':

            # Remove new line characters from line
            line = line.rstrip("\n")

            # Remove space at beginning of string
            passportStringToDict = passportStringToDict[1:]

            # Add beginning of dict
            passportString = '{'

            # Split string by passport key
            split = passportStringToDict.split()

            # Add double quotes around key/values so string can be converted to JSON
            for i in split:
                key = i.split(':')[0]
                value = i.split(':')[1]
                key = '"' + key + '"'
                value = '"' + value + '"'

                # create new key/value pair with comma and space at end
                newKeyValPair = key + ' : ' + value + ', '

                # append new key/value pair to string that will be converted to JSON
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

                # Get passport attributes for validation
                byr = passportDict['byr']
                iyr = passportDict['iyr']
                eyr = passportDict['eyr']
                hgt = passportDict['hgt']
                hcl = passportDict['hcl']
                ecl = passportDict['ecl']
                pid = passportDict['pid']

                # Birth Year (byr) - at least 1920 and at most 2002
                if int(byr) >= 1920 and int(byr) <= 2002:
                    # Issue Year (iyr) - at least 2010 and at most 2020
                    if int(iyr) >= 2010 and int(iyr) <= 2020:
                        # Expiration Year - at least 2020 and at most 2030
                        if int(eyr) >= 2020 and int(eyr) <= 2030:
                            # Height could be in cm or in
                            if 'cm' in hgt:
                                # Get number separate from label
                                num = hgt.rstrip("cm")
                                # Height (hgt) - at least 150 and at most 193
                                if int(num) >= 150 and int(num) <= 193:
                                    hclFirst = hcl[0]
                                    hclNum = hcl[1:]
                                    # Hair Color (hcl) - first character must be # followed by 6 digits in 0-9 and a-f
                                    if hclFirst == '#':
                                        for i in hclNum:
                                            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                                                         'c', 'd', 'e', 'f']:
                                                break
                                        # Eye Color (ecl) - must be in acceptable list
                                        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                            # Passport Id (pid) must be 9 digits including leading zeros
                                            if len(pid) == 9:
                                                validPassports += 1

                            # Height could be in cm or in
                            elif 'in' in hgt:
                                # Get number separate from label
                                num = hgt.rstrip("in")
                                # Height (hgt) - at least 59 and at most 76
                                if int(num) >= 59 and int(num) <= 76:
                                    hclFirst = hcl[0]
                                    hclNum = hcl[1:]
                                    if hclFirst == '#':
                                        for i in hclNum:
                                            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                                                         'c', 'd', 'e', 'f']:
                                                break
                                        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                            if len(pid) == 9:
                                                validPassports += 1

            # Reset passport string container after validation has completed
            passportStringToDict = ''
            continue

        line = line.rstrip("\n")

        # Append line to string container with space separating each line
        passportStringToDict += ' ' + line

    print('Valid Passports: ' + str(validPassports))

if __name__ == '__main__':
    findValidPassports()
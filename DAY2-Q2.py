def findValidPasswords():
    validPasswords = 0

    f = open("day2-q1-input.txt", "r")
    for line in f:
        split = line.split()
        charCount = split[0].split('-')
        passwordLetter = split[1].split(':')[0]
        password = split[2]

        passwordContainsLetter = 0
        for index, letter in enumerate(password):
            if index + 1 == int(charCount[0]):
                if letter == passwordLetter:
                    passwordContainsLetter += 1

            if index + 1 == int(charCount[1]):
                if letter == passwordLetter:
                    passwordContainsLetter += 1

        if passwordContainsLetter > 0 and passwordContainsLetter < 2:
            validPasswords += 1

    f.close()
    return validPasswords


if __name__ == '__main__':
    print(findValidPasswords())

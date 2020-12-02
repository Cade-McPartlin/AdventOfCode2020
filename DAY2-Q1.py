def findValidPasswords():
    validPasswords = 0

    f = open("day2-q1-input.txt", "r")
    for line in f:
        split = line.split()
        charCount = split[0].split('-')
        passwordLetter = split[1].split(':')[0]
        password = split[2]

        letterCount = 0
        for letter in password:
            if letter == str(passwordLetter):
                letterCount += 1

        if letterCount >= int(charCount[0]) and letterCount <= int(charCount[1]):
            validPasswords += 1

    f.close()
    return validPasswords


if __name__ == '__main__':
    print(findValidPasswords())



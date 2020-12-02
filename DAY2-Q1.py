# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter
# must appear for the password to be valid. For example, '1-3 a' means that the password
# must contain 'a' at least 1 time and at most 3 times.
# Example:
# 1-3 a: abcde  -- valid
# 1-3 b: cdefg  -- not valid
# 2-9 c: ccccccccc  -- valid
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



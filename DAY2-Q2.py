# Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second character, and so on.
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter.
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
# Example
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
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

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
        # Break up each line of text file into array
        split = line.split()
        # Get the range for how many times the letter can be in the password
        charCount = split[0].split('-')
        # Get password letter that we are looking for
        passwordLetter = split[1].split(':')[0]
        # Get password
        password = split[2]

        # Counter for number of times the letter appears at specific indexes
        passwordContainsLetter = 0
        for index, letter in enumerate(password):

            # If the current index of the letter = the first index where a letter can be,
            # validate if the letter at this index = the password letter
            if index + 1 == int(charCount[0]):
                if letter == passwordLetter:
                    passwordContainsLetter += 1

            # If the current index of the letter = the last index where a letter can be,
            # validate if the letter at this index = the password letter
            if index + 1 == int(charCount[1]):
                if letter == passwordLetter:
                    passwordContainsLetter += 1

        # Validate if greater than 0 of the indexes and less than both of the indexes
        # contained the letter. If so, the password is valid
        if passwordContainsLetter > 0 and passwordContainsLetter < 2:
            validPasswords += 1

    f.close()
    return validPasswords


if __name__ == '__main__':
    print(findValidPasswords())

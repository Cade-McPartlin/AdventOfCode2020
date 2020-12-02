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

        # Break up each line of text file into array
        split = line.split()
        # Get the range for how many times the letter can be in the password
        charCount = split[0].split('-')
        # Get password letter that we are looking for
        passwordLetter = split[1].split(':')[0]
        # Get password
        password = split[2]

        letterCount = 0
        for letter in password:
            # Count how many times the password letter is in the password
            if letter == str(passwordLetter):
                letterCount += 1

        # If the letter is in the password more than or equal to the minimum and
        # less than or equal to the maximum, it is a valid password
        if letterCount >= int(charCount[0]) and letterCount <= int(charCount[1]):
            validPasswords += 1

    f.close()
    return validPasswords


if __name__ == '__main__':
    print(findValidPasswords())



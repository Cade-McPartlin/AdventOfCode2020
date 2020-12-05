# https://adventofcode.com/2020/day/3
# Determine the number of trees you would encounter if,
# for each of the following slopes, you start at the top-left corner
# and traverse the map all the way to the bottom:
#
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.) (Question 1)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
#
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
def countNumberOfTrees(spacesToRight, spacesDown=1):
    f = open('Day3-input.txt', 'r')

    # Get file lines separate from file so that I can change the iterator
    fileLines = f.readlines()

    # Position tracker to simulate rows of trees continuing infinitely to the right
    position = 0

    # Total trees encountered
    treeCount = 0

    # Iterate over the fileLines with an iterator of spacesDown (i.e. every 2nd row)
    fileLines = fileLines[::spacesDown]

    # Loop over file lines, which have already been limited by spacesDown
    for index, line in enumerate(fileLines):

        # Remove \n characters from the end of each line
        line = line.rstrip("\n")

        # print('index: ' + str(index) + ' Position: ' + str(position) + ' Length of line: ' + str(len(line)) + ' Character: ' + line[position])

        # skip first line of file since we have to move down at least one row
        if index == 0:
            position += spacesToRight
            continue

        # Count all trees (#) encountered
        if line[position] == '#':
            treeCount += 1

        # If the new position will be greater than or equal to the length of the line,
        # find the difference between the new position and the length of the line
        # and set the position equal to the difference
        #
        # This logic simulates the rows continuing in the same pattern to the right infinitely
        # by resetting the index to a value within the length of the line
        if position + spacesToRight >= len(line):
            difference = (position + spacesToRight) - len(line)
            # print('position + spacesToRight: ' + str(position + spacesToRight))
            # print('difference ' + str(difference))

            # Reset position to the difference
            position = difference

            # print('position reset: ' + str(position))
            continue

        # Increment position by spacesToRight
        position += spacesToRight

    print('Right: ' + str(spacesToRight) + ' Down: ' + str(spacesDown) + ' Tree Count: ' + str(treeCount))

    f.close()

    # Return tree count
    return treeCount


if __name__ == '__main__':

    # Multiply number of trees for each slope to get product
    totalTrees = countNumberOfTrees(1) \
                 * countNumberOfTrees(3) \
                 * countNumberOfTrees(5) \
                 * countNumberOfTrees(7) \
                 * countNumberOfTrees(1, 2)
    print('Product of all Trees: ' + str(totalTrees))

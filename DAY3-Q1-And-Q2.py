def countNumberOfTrees(spacesToRight, spacesDown=1):
    f = open('Day3-input.txt', 'r')

    fileLines = f.readlines()
    position = 0
    treeCount = 0

    fileLines = fileLines[::spacesDown]

    for index, line in enumerate(fileLines):
        line = line.rstrip("\n")
        # print('index: ' + str(index) + ' Position: ' + str(position) + ' Length of line: ' + str(len(line)) + ' Character: ' + line[position])

        # skip first line of file
        if index == 0:
            position += spacesToRight
            continue

        if line[position] == '#':
            treeCount += 1

        if position + spacesToRight >= len(line):
            difference = (position + spacesToRight) - len(line)
            # print('position + spacesToRight: ' + str(position + spacesToRight))
            # print('difference ' + str(difference))
            position = difference
            # print('position reset: ' + str(position))
            continue

        position += spacesToRight

    print('Right: ' + str(spacesToRight) + ' Down: ' + str(spacesDown) + ' Tree Count: ' + str(treeCount))

    f.close()
    return treeCount

if __name__ == '__main__':
    totalTrees = countNumberOfTrees(1)\
                 * countNumberOfTrees(3)\
                 * countNumberOfTrees(5)\
                 * countNumberOfTrees(7)\
                 * countNumberOfTrees(1, 2)
    print('Product of all Trees: ' + str(totalTrees))

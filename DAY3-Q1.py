def countNumberOfTrees():
    f = open('Day3-input.txt', 'r')

    position = 0
    treeCount = 0
    for index, line in enumerate(f):
        line = line.rstrip("\n")
        print('index: ' + str(index) + ' Position: ' + str(position) + ' Length of line: ' + str(len(line)) + ' Character: ' + line[position])

        # skip first line of file
        if index == 0:
            position += 3
            continue

        if line[position] == '#':
            treeCount += 1

        if position + 3 >= len(line):
            difference = (position + 3) - len(line)
            print('position + 3: ' + str(position + 3))
            print('difference ' + str(difference))
            position = difference
            print('position reset: ' + str(position))
            continue

        position += 3

    print('Tree Count: ' + str(treeCount))

if __name__ == '__main__':
    countNumberOfTrees()
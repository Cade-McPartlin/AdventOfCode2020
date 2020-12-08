
def runGameLoop(accumulator, file):

    lines = file.readlines()

    accumulator = 0
    indexsHit = []
    indexTracker = 0
    iterations = 0

    while True:

        print('index tracker: ' + str(indexTracker))
        if indexTracker in indexsHit:
            print('FINAL Accumulator before infinite loop: ' + str(accumulator))
            break

        indexsHit.append(indexTracker)

        if indexTracker < 0:
            index = len(lines) - indexTracker
            line = lines[index]
        else:
            line = lines[indexTracker]
        print(line)

        # no operation, do nothing
        if 'nop' in line:
            indexTracker += 1
            iterations += 1
            continue

        # move ahead x operations, and increase the value of the accumulator by x
        if 'acc' in line:
            number = line.split(' ')[1]
            if '+' in number:
                number = number[1:]
                accumulator += int(number)
                indexTracker += 1
            elif '-' in number:
                number = number[1:]
                accumulator -= int(number)
                indexTracker += 1

            iterations += 1
            print('accumulator: ' + str(accumulator))
            continue

        # jump forward/backwards x operations
        if 'jmp' in line:
            number = line.split(' ')[1]

            if '+' in number:
                number = number[1:]
                indexTracker += int(number)
            if '-' in number:
                number = number[1:]
                indexTracker -= int(number)
            iterations += 1
            continue

if __name__ == '__main__':
    accumulator = 0

    file = open('day8-input.txt', 'r')

    runGameLoop(accumulator, file)


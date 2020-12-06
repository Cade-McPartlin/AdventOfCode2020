import math

# https://adventofcode.com/2020/day/5
def findSeat():
    f = open('day5-input.txt', 'r')

    seatIds = []

    for line in f:
        # print(line)
        line = line.rstrip("\n")

        rowNumList = []
        colNumList = []
        rowNumberRange = 128
        colNumberRange = 8
        row = -1
        col = -1

        # add numbers 0-127 to rowNumList
        for i in range(128):
            rowNumList.append(i)

        # add numbers 0-7 to colNumList
        for i in range(8):
            colNumList.append(i)

        for i in line:

            if len(rowNumList) == 1:
                row = rowNumList[0]

                # Get half of the current number range
                colNumberRange = math.floor(colNumberRange / 2)

                '''Determine col'''
                # Take lower half of numbers
                if i == 'L':
                    colNumList = colNumList[:colNumberRange]
                # Take upper half of numbers
                if i == 'R':
                    colNumList = colNumList[colNumberRange:]

            # Get half of the current number range
            rowNumberRange = math.floor(rowNumberRange / 2)

            '''Determine row'''
            # Take lower half of numbers
            if i == 'F':
                rowNumList = rowNumList[:rowNumberRange]
            # Take upper half of numbers
            if i == 'B':
                rowNumList = rowNumList[rowNumberRange:]

        col = colNumList[0]

        # Every seat also has a unique seat ID: multiply the row by 8, then add the column
        seatId = (row * 8) + col
        seatIds.append(seatId)
        # print('row: ' + str(row) + ' col: ' + str(col) + ' seat id: ' + str(seatId))

    f.close()

    seatIds.sort()

    # Determine our seat number
    # the seats with IDs +1 and -1 from yours will be in your list.
    # compare index with number next in array
    for index, num in enumerate(seatIds):
        if index + 1 < len(seatIds):
            secondNum = seatIds[index + 1]

            # if the difference between the current number and the next number > 1,
            # then your seat is the number in between
            if secondNum - num > 1:
                print('num1: ' + str(num))
                print('num2: ' + str(secondNum))

                print('Your seatId: ' + str(num + 1))

    # print('seatIds: ' + str(seatIds))
    print('Max seatId: ' + str(max(seatIds)))


if __name__ == '__main__':
    findSeat()

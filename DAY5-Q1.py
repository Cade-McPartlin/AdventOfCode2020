import math

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

                colNumberRange = math.floor(colNumberRange / 2)

                # Determine col
                # Take lower half of numbers
                if i == 'L':
                    colNumList = colNumList[:colNumberRange]
                # Take upper half of numbers
                if i == 'R':
                    colNumList = colNumList[colNumberRange:]




            # Get half of the current number range
            rowNumberRange = math.floor(rowNumberRange / 2)

            # Determine row
            # Take lower half of numbers
            if i == 'F':
                rowNumList = rowNumList[:rowNumberRange]
            # Take upper half of numbers
            if i == 'B':
                rowNumList = rowNumList[rowNumberRange:]

        col = colNumList[0]

        # seat id = row * 8 + col
        seatId = (row * 8) + col
        seatIds.append(seatId)
        print('row: ' + str(row) + ' col: ' + str(col) + ' seat id: ' + str(seatId))

    f.close()

    print(seatIds)
    print('Max seatId: ' + str(max(seatIds)))

if __name__ == '__main__':
    findSeat()
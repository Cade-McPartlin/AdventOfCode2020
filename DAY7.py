
def countShinyGoldBags(lines, bagName, masterContainers, containerBags):
    print('running')
    linesToRemove = []

    for line in lines:
        if bagName in line:

            bagIndex = line.find(bagName)

            containerBag = ' '

            # get container bag from beginning of line
            containerBag = containerBag.join(line.split()[:3])

            # Remove potential plural from string so we can
            # find singular cases in next search
            if containerBag[-1] == 's':
                containerBag = containerBag[:-1]

            if containerBag != 'shiny gold bag':
                containerBags.add(containerBag)
                masterContainers.add(containerBag)
                linesToRemove.append(line)

    # Remove lines
    for line in linesToRemove:
        lines.remove(line)

    if len(containerBags) == 0:
        return masterContainers
    countShinyGoldBags(lines, containerBags.pop(), masterContainers, containerBags)


if __name__ == '__main__':
    f = open('day7-input.txt', 'r')
    lines = f.readlines()
    f.close()
    masterContainers = set()
    containerBags = set()
    countShinyGoldBags(lines, 'shiny gold bag', masterContainers, containerBags)
    print('Master Containers: ' + str(masterContainers))
    print('Count Master Containers: ' + str(len(masterContainers)))

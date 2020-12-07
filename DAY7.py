
def countShinyGoldBags(lines, bagName, masterContainers, containerBags):
    print('running')
    linesToRemove = []

    for line in lines:
        if bagName in line:
            containerBag = ' '
            # get container bag from beginning of line
            containerBag = containerBag.join(line.split()[:3])

            # Remove potential plural from string so we can
            # find singular cases in next search
            if containerBag[-1] == 's':
                containerBag = containerBag[:-1]

            if containerBag != 'shiny gold bag':
                # Add bag to container bag for future searches
                containerBags.add(containerBag)
                # Add bag to master container since it can hold a shiny gold bag
                masterContainers.add(containerBag)
                # add line to linesToRemove
                linesToRemove.append(line)

    # Remove lines to create a new subset to search through
    for line in linesToRemove:
        lines.remove(line)

    # once there are no more bags to search for, return the master container
    if len(containerBags) == 0:
        return masterContainers

    # Call method recursively, pass in new subset of line,
    # bag name, master container of bags that hold shiny gold bag,
    # and new subset of container bags
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

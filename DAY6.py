# https://adventofcode.com/2020/day/6
def findQuestionCount():

    f = open('day6-input.txt', 'r')

    anyQuestionsAnsweredYes = set()
    totalAnyQuestionsAnsweredYes = 0
    totalAllQuestionsAnsweredYes = 0
    allQuestionsAnsweredYes = list()
    personInGroupCount = 0
    for line in f:

        # New line signals end of group, so determine questions they answered yes to
        if line == '\n':
            # print('Questions answered yes: ' + str(anyQuestionsAnsweredYes))
            # print('Count questions answered yes: ' + str(len(anyQuestionsAnsweredYes)))

            # print('All questions answered yes: ' + str(allQuestionsAnsweredYes))

            # list of all possible questions
            questionList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

            # loop over possible questions
            for letter in questionList:

                # get count of how many times question appears in list of questions answered yes
                letterCount = allQuestionsAnsweredYes.count(letter)

                # if the question count matches how many people are in the group,
                # add 1 to all questions answered yes
                if letterCount == personInGroupCount:
                    totalAllQuestionsAnsweredYes += 1

            # The total of any questions answered yes is the length of the set
            # since sets are unique values only
            totalAnyQuestionsAnsweredYes += len(anyQuestionsAnsweredYes)

            # reset set for next run
            anyQuestionsAnsweredYes = set()

            # reset list for next run
            allQuestionsAnsweredYes = list()

            # reset count for next run
            personInGroupCount = 0
        else:

            line = line.rstrip('\n')

            # Q2 set
            personInGroupCount += 1
            for i in line:
                allQuestionsAnsweredYes.append(i)

            # Q1 set
            for i in line:
                anyQuestionsAnsweredYes.add(i)


    f.close()

    print('Total ANY questions answered yes: ' + str(totalAnyQuestionsAnsweredYes))
    print('Total ALL questions answered yes: ' + str(totalAllQuestionsAnsweredYes))

if __name__ == '__main__':
    findQuestionCount()
def findQuestionCount():

    f = open('day6-input.txt', 'r')


    questionsAnsweredYes = set()
    totalQuestionsAnsweredYes = 0
    for line in f:

        # New line signals end of group, so determine questions they answered yes to
        if line == '\n':
            # print('Questions answered yes: ' + str(questionsAnsweredYes))
            print('Count questions answered yes: ' + str(len(questionsAnsweredYes)))
            totalQuestionsAnsweredYes += len(questionsAnsweredYes)
            questionsAnsweredYes = set()
        else:

            line = line.rstrip('\n')
            # print(line)

            for i in line:
                questionsAnsweredYes.add(i)


    f.close()

    print('Total questions answered yes: ' + str(totalQuestionsAnsweredYes))

if __name__ == '__main__':
    findQuestionCount()
def questionWhichAnyoneAnsweredYes(previousQuestions, nextQuestions):
    return set(set(previousQuestions) | set(nextQuestions))


def questionWhichEveryoneAnsweredYes(previousQuestions, nextQuestions):
    return set(set(previousQuestions) & set(nextQuestions))


def countOfQuestionsInAGroupAnsweredYes(individualAnswers, questionAggregartor):
    sumOfQuestionsInAGroupAnsweredYes = 0
    questionsInAGroupAnsweredYes = None
    for individualAnswer in individualAnswers:
        if individualAnswer == "":
            sumOfQuestionsInAGroupAnsweredYes = sumOfQuestionsInAGroupAnsweredYes+len(questionsInAGroupAnsweredYes)
            questionsInAGroupAnsweredYes = None
        elif questionsInAGroupAnsweredYes is None:
            questionsInAGroupAnsweredYes = set(individualAnswer)
        else:
            questionsInAGroupAnsweredYes = questionAggregartor(questionsInAGroupAnsweredYes, set(individualAnswer))

    if len(questionsInAGroupAnsweredYes) > 0:
        sumOfQuestionsInAGroupAnsweredYes = sumOfQuestionsInAGroupAnsweredYes+len(questionsInAGroupAnsweredYes)

    return sumOfQuestionsInAGroupAnsweredYes

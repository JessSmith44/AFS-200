import itertools
import random

class TriviaQuestion():

    def __init__(self, question, category, diffLevel, correctAns, incorrectAns, id_iter):
        self.question = question
        self.category = category
        self.diffLevel = diffLevel
        self.correctAns = correctAns
        self.incorrectAns = incorrectAns
        self.id_iter = id_iter

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getDiffLevel(self):
        return self.diffLevel

    def getCorrectAns(self):
        return self.correctAns

    def getIncorrectAns(self):
        return self.incorrectAns

    def getId(self):
        return self.id_iter

    # def answersList(self, correctAns, incorrectAns):
    #     questionList = correctAns, incorrectAns
    #     return questionList

    def getShuffledAnswers(self):
        # shuffledList = []
        # for answers in self.answersList:
        #     shuffledList = random.shuffle(questionList)
            
        questionList = self.incorrectAns
        questionList.append(self.correctAns)
        # print(questionList) 
        random.shuffle(questionList)
        # print(questionList)
        return questionList

    # should return a list of all correct answers and incorrect 
    # answers in a list that has been shuffled. Google "python shuffle list"
    # for information on how to shuffle a list. This class will be used
    # to store a single trivia question

    def __str__(self):
        retstr = self.question
        retstr += " "
        retstr += self.correctAns
        retstr += " "
        retstr += str(self.incorrectAns)
        # print(retstr)
        return retstr
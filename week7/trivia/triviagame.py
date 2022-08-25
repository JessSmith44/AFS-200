

class TriviaGame():
    def __init__(self):
        self.questions = []
    # this class is used to store multiple trivia questions
    # that are retrieved from an API. This class needs at
    # least one attribut to store the questions in a list
 
    def addQuestions(self, question):
        self.questions.append(question)

    def getAllQuestions(self):
        # to retrieve all questions
        return self.questions

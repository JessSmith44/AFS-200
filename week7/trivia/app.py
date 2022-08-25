from flask import Flask, request, render_template
import requests
import json
from socket import timeout
from urllib import response
from triviagame import TriviaGame 
from triviaquestion import TriviaQuestion
import itertools

def getData(triviaQuestions):
    URL = "https://opentdb.com/api.php?amount=7&category=27&type=multiple"

    try:
        response = requests.get(URL, timeout=25)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    print(triviaQuestions, "line 27 print")


theTriviaGame = TriviaGame()

jsonData = getData("triviaQuestions")

idCounter = 0

for data in jsonData["results"]:
    question = data["question"]
    correctAns = data["correct_answer"]
    incorrectAns = data["incorrect_answers"] 
    category = data["category"]
    diffLevel = data["difficulty"]
    id_iter = idCounter

    newQuestion = TriviaQuestion(question, category, diffLevel, correctAns, incorrectAns, id_iter)
    
    theTriviaGame.addQuestions(newQuestion) 
    idCounter += 1
 
theTriviaGame.getAllQuestions()


app = Flask(__name__)

@app.route("/")
def home():
    # Display trivia questions to the player with multiple choice radio buttons under each question.
    # get trivia questions
    myTrivia = theTriviaGame.getAllQuestions()
    # myTriviaAns = theTriviaGame.getShuffledAnswers()
    return render_template("displayQs.html", results = myTrivia)
    # return ("trivia game")

# http://127.0.0.1:5000/score (Method is POST)
# Retrieve the user selected answers to each question
# Determine which questions were answered correctly and which were 
# answered incorrectly.Display the results to the user.

@app.route("/score", methods = ["POST"])
def getScore():
    # for loop to iterate through questions
    myTrivia = theTriviaGame.getAllQuestions()
    correctQuestion = []
    incorrectQuestion = []
    for question in myTrivia:

        inputValue = request.form.get(str(question.id_iter))

        if(inputValue == question.correctAns):
            correctQuestion.append(question)
        else:
            incorrectQuestion.append(question)

    # results = [incorrectQuestion, correctQuestion]
    results = {"correct": correctQuestion, "incorrect": incorrectQuestion}
    return render_template('answers.html', results = results)

if __name__ == "__main__":
    app.run()
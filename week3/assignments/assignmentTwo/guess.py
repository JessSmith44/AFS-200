mySecretWord = "ABROAD"
copyWord = mySecretWord

guessedLetters = []

wordBoard=['_']*len(mySecretWord)
wordBoard

# showBoard = "Can you guess the secret word?" + str(wordBoard)
def showBoard():
    print(" ".join(wordBoard))

def checkGuess(guess, mySecretWord, wordBoard):
    index = mySecretWord.find(guess)
    while index != -1:
        if guess in mySecretWord:
            index = mySecretWord.find(guess)
            removed_character='*'
            mySecretWord = mySecretWord[:index]+removed_character+mySecretWord[index+1:]
            wordBoard[index] = guess
        else:
            index = -1
    return (mySecretWord, wordBoard)

def win_check():
    for i in range(0, len(wordBoard)):
        if wordBoard[i] == '_':
            return -1
    return 1

print("Can you guess the secret word?")

num_turns = 5

while (num_turns):
    showBoard()
    guesses = input("Guess a character: ").upper()

    if guesses in mySecretWord:
        mySecretWord, wordBoard = checkGuess(guesses, mySecretWord, wordBoard)
        guessedLetters.append(guesses)
        # print(wordBoard)
    elif guesses in guessedLetters: 
        print("Oh-no! You already guessed " +guesses)
        num_turns = num_turns
    else:
        print("Sorry that letter is not in the word.")
        num_turns = num_turns-1
        guessedLetters.append(guesses)

    if win_check() == 1:
        num_turns = 0
        print("Congratulations you won! " +copyWord)
    elif num_turns == 0:
        print("Oh no! I am sorry, you lost!")
    
    print("You have " +str(num_turns)+ " turns left.")
    print()

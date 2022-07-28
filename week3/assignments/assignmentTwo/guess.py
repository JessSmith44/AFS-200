mySecretWord = "ABROAD"
copyWord = mySecretWord
# Create a variable of list type to store the guessed letters by the user
#
#guessed letters not storing, local issue area and fix
guesses = []
print(guesses)

wordBoard=['_']*len(mySecretWord)
wordBoard

showBoard = "Can you guess the secret word?" + str(wordBoard)

def checkGuess(guess, mySecretWord, wordBoard):
    index = -2

    while index != -1:
        if guess in mySecretWord:
            index = mySecretWord.find(guess)
        # should return boolean true or false, not sure if its working SMH
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

print(showBoard)

# If the user already guessed that letter, let the user know that

num_turns = 5

while (num_turns):
    guesses = input("Guess a character: ").upper()

    if guesses in mySecretWord:
        mySecretWord, wordBoard = checkGuess(guesses, mySecretWord, wordBoard)
        print(wordBoard)
    else: 
        print("Sorry that letter is not in the word.")
        num_turns = num_turns-1

    if win_check() == 1:
        print("Congratulations you won! " +copyWord)
    elif num_turns == 0:
        print("Oh no! I am sorry, you lost!")

    print("You have " +str(num_turns)+ " turns left.")
    print()

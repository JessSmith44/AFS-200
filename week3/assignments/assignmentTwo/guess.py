secretWord = "Classical"

# Create a variable of list type to store the guessed letters by the user
guessedltrs = []
print(guessedltrs)
# Create a variable called “wordBoard” of list type whose initial size is the length of your secret word.  The value of each list item should initially be “ _ “
wordBoard=['_']*len(secretWord)
wordBoard

# Create a function called “showBoard” that will display the current board state which is stored in the variable “wordBoard”

# Create a function called “checkGuess”. 
# This function requires one parameter, the user’s guessed letter.
def get_letter_position(guess, secretWord, wordBoard):
    index = -2

    while index != -1:
        if guess in secretWord:
            index = secretWord.find(guess)

            removed_character='*'
            secretWord = secretWord[:index]+removed_character+secretWord[index+1:]
            wordBoard[index] = guess

        else:
            index = -1
    return (secretWord, wordBoard)
# This function should check if the guessed letter is in the secret word.  If it is, then update “wordBoard” by placing the correctly guessed letter in the correct position.
# Remember that a word may have more than one instance of the guessed letter.
# This function should return a Boolean value of True if the letter was found, otherwise False.
def win_check():
    for i in range(0, len(wordBoard)):
        if wordBoard[i] == '_':
            return -1
    return 1
# Display the board to the user
displayBoard = "Can you guess the secret word?" + str(wordBoard)
print(displayBoard)
# Prompt the user to guess a letter
# If the user already guessed that letter, let the user know that

# If the letter is not in the secret word, keep track of the number of wrong guesses.  When the user has five wrong guesses and the word hasn’t yet been guessed, then the game ends.
# If the user has guessed all of the letters, the game ends.  Display the fully solved board to the user.
num_turns = len(secretWord)
for i in range(0, num_turns):
    guessedltrs = input("Guess a character: ")

    if guessedltrs in secretWord:
        secretWord, wordBoard = get_letter_position(guessedltrs, secretWord, wordBoard)
        print(wordBoard)
    else: 
        print("Sorry that letter is not in the word.")

    if win_check() == 1:
        print("Congratulations you won! " +secretWord)
        break

    print("You have " +str(num_turns -i)+ " turns left.")
    print()

# Hint: You will find it easier if the word and all of the user guesses are uppercase.
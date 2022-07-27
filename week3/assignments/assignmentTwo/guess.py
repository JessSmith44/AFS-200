# Create a variable and assign it the value of a word to be guessed by the user. This should be a single word with at least 6 characters
secretWord = "Classical"
# Create a variable of list type to store the guessed letters by the user

# Create a variable called “wordBoard” of list type whose initial size is the length of your secret word.  The value of each list item should initially be “ _ “
wordBoard=['_']*len(secretWord)
wordBoard
# Create a function called “showBoard” that will display the current board state which is stored in the variable “wordBoard”

# Create a function called “checkGuess”. 
# This function requires one parameter, the user’s guessed letter.

# This function should check if the guessed letter is in the secret word.  If it is, then update “wordBoard” by placing the correctly guessed letter in the correct position.
# Remember that a word may have more than one instance of the guessed letter.
# This function should return a Boolean value of True if the letter was found, otherwise False.

# Display the board to the user

# Prompt the user to guess a letter
# If the user already guessed that letter, let the user know that
# If the letter is in the secret word, display the updated board with the letters in the correct place
# If the letter is not in the secret word, keep track of the number of wrong guesses.  When the user has five wrong guesses and the word hasn’t yet been guessed, then the game ends.
# If the user has guessed all of the letters, the game ends.  Display the fully solved board to the user.

# Continue prompting the user till they run out of chances or solve the puzzle.

# Hint: You will find it easier if the word and all of the user guesses are uppercase.
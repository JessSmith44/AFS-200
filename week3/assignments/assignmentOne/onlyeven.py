
# USE while loop AND create function to call in the while loop


userinput = input("Please enter a positive number: ")

def evenInputs(userinput):
    if (int(userinput) % 2 == 0):
        evenInputs = [evens for evens in range(int(userinput)) if evens %2 == 0]
        print(evenInputs)


if (userinput.isdigit() == False):
    userinput = input("Invalid input. Please enter a positive number: ")


while (int(userinput.isdigit() == True)):
    if (int(userinput) % 2 != 0):
        userinput = input("Invalid input. Please enter a positive number: ")
    if(int(userinput) % 2 == 0):
        evenInputs(userinput)
        break

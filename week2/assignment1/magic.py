
# Complete the following operations:
# Prompt the user to input a number.

message = int(input('Please enter a number: '))

# Multiple this number by 3.
# Add 6 to the number
# Divide the new number by 3.
# Subtract the number from step 1 from the answer in step 4.

newmsg = ((((message * 3) + 6) // 3) - message)

# Display the results as an integer.  The results should always be 2. 

print(newmsg)
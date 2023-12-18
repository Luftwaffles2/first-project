import random

high=0
low=0
win=0
num_guesses=high+low+win
guess_range = 99
answer= random.randint(1, guess_range)
userInput=input

print("This is a game where you will guess a random number!")
guess=userInput

while(True): 
    userInput = int(input("Please guess a number between 1 and 99:"))

    if userInput>answer:
        print ("Too high, try again.")
        high += 1

    elif userInput == answer:
        print ("You got it correct! Congratulations!")
        win += 1
        break 
   
    elif userInput<answer:
        print ("Too low, try again.")
        low += 1

print()
print("Number of times too high:", high)
print("Number of times too low:", low)
print("Total number of guesses:", (num_guesses))
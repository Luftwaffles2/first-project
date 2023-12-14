import random

num_guesses=0
guess_range = 99
answer= random.randint(1, guess_range)

print("This is a game where you will guess a random number!")
print; ""
userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
guess=int(userInput)

while(True): 
    userInput = int(input("Please guess a number between 1 and 99:"))


    if guess<answer:
     print("The number is higher")


    elif guess==answer:
     print ("You guessed it!")
    
    
    else :guess>answer
    print ("The number is lower")
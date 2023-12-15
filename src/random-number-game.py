import random

num_guesses=0
guess_range = 99
answer= random.randint(1, guess_range)
userInput=input

print("This is a game where you will guess a random number!")
guess=userInput

while(True): 
    userInput = int(input("Please guess a number between 1 and 99:"))

    if userInput > answer:
        print ("Too high, try again.")
        num_guesses + 1

    elif userInput == answer:
        print ("You got it correct! Congratulations!")
        num_guesses + 1
        break 
    print (num_guesses)
   
    if userInput<answer:
        print ("Too low, try again.")
    num_guesses + 1
        
import random

guess_range = 99
answer= random.randint(1, guess_range)

print("This is a game where you will guess a random number!")
print; ""
userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
guess=int(userInput)

guess= ""
while guess < answer:
 print("The number is lower")
 if guess>answer:
  print("The number is higher")
 if guess==answer:
  print("You guessed it!")


# The Perfect Guess

'''
We will write a program that generates a random number & asks the user to guess it
If the player's guess is higher than actual number the program displays lower number please
if the user's guess is too low the program prints higher number please
if the numbers are same the program displays the number
'''

import random

randomNumber = random.randint(1, 100)
print(randomNumber)
userGuess = None
guesses = 0

while(userGuess != randomNumber):

    userGuess = int(input("Enter your guess: "))
    guesses+= 1
    if (userGuess == randomNumber):
        print("Congratulations! Your guess is right")
    else:
        if(userGuess>randomNumber):
            print("Oops!! you guessed it wrong.Please enter a smaller number")
        else:
            print("Oops!! you guessed it wrong.Please enter a larger number")

print(f"You guessed the number after {guesses} attempts.")


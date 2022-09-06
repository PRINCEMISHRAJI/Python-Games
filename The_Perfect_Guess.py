''' This Game is created for free use
    Everyone can make copies or reuse it in any way 
    Made By - Ankit Mishra'''

import random

randomNumber = random.randint(1, 100)

guessNo = int(input("Enter your guess from 1 to 100: "))

guessCounter = 1  # Counts the number of guesses required to make the perfect guess

while guessNo != randomNumber:
    guessCounter += 1
    if guessNo > randomNumber:
        guessNo = int(input(" You guessed larger number, Guess a smaller number instead: "))
    elif guessNo < randomNumber:
        guessNo = int(input(" You guessed smaller number, Guess a larger number instead: "))

if guessNo == randomNumber:
    print(f"\t ****** Congratulations you guessed it right in {guessCounter} guesses ******")

#   Checking if previous score exists, and if yes automatically overwrites the new highscore
with open('maxscore.txt') as f:
    reading = int(f.read())
    # You need to create a "maxscore.txt" file in your folder and put 101 in it so that our program can read inputs from it for once
if reading > guessCounter:
    with open("maxscore.txt", "w") as f:
        f.write(str(guessCounter))
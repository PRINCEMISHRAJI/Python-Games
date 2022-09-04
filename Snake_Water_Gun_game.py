#UNLICENSED 
# MADE BY ANKIT MISHRA
#  NEW PUSHES AND FEATURES WILL BE ADDED ONCE REQUESTED
# IF YOU READING THIS APPRECIATE, I'D REVISED PYTHON YESTERDAY AND BUILD THIS GAME USING THE MOST BASIC THINGS IN PROGRAMMING AND PYTHON 


import random
import sys

def playgame(playerChoice):
    print("CPU Turn: CPU deciding its choice from (G) Gun - (S) Snake - (W) Water ")
    CPU = [ "G", "S", "W"]
    randChoice = random.choice(CPU)


    if (playerChoice == "G" or playerChoice == "g") and (randChoice == "S" or randChoice == "s"):
        print("\t Congratulations, You won!!!!!!")
    elif (playerChoice == "S" or playerChoice == "s") and (randChoice == "W" or randChoice == "w"):
        print("\t Congratulations, You won!!!!!!")
    elif (playerChoice == "W" or playerChoice == "w") and (randChoice == "G" or randChoice == "g"):
        print("\t Congratulations ;), You won!!!!!!")
    elif playerChoice == randChoice:
        print("\t Attention!! It's a tie, Try Again :)")
    else:
        print("\t Unfortunately, You Lose!!!!!!")

    print(f"CPU choice was {randChoice} and Player choice is {playerChoice} " )


    playagain = input("Do you want to play the game again ?? Press 'Y' for YES and 'N' for NO : " )
    if playagain == "Y" or playagain == "y":
            playerChoice = input("Player Turn: Enter Your Choice (G) Gun - (S) Snake - (W) Water : ")

            playgame(playerChoice)
    elif playagain == "N" or playagain == "n" :
            sys.exit("Game is now exiting")


playerChoice = input("Player Turn: Enter Your Choice (G) Gun - (S) Snake - (W) Water : ")

playgame(playerChoice)


# I APPRECIATE YOU FOR SPENDING YOUR VALUABLE TIME HERE
import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 10
while attempts<max_attempts:
    guess=int(input("Guess a number between 1 and 100:"))
    attempts+=1
    if guess==number:
        print("Correct!You guessed the number")
        print("Attempts:",attempts)
        break
    elif(guess<number):
        print("Too low!try again.")
    else:
        print("Too high!Try again.")
    play_again=input("Do you want to play again? (yes/no):").lower()
    if play_again!="yes":
        print("Thanks for playing")
        break
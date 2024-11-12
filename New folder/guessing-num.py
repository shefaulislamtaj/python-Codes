
import random

for x in range(1, 60):
    guessNumber = int(input("Enter a number between 1 and 5: "))
    randomNumber = random.randint(1, 5)
    
    if guessNumber == randomNumber:
        print("You won!")
    else:
        print("You lost. The correct number was", randomNumber)

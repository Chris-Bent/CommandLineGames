import datetime
import random

def main():
    print("\nWelcome to\nNUMBER GUESS\n")
    print("*RULES*\n")
    
    number = random.randint(1, 100)
    numGuesses = 0
    attemptCount = 0

    print("SELECT DIFFICULTY:\nEASY(1)\nMEDIUM(2)\nHARD(3)")
    playerDifficulty = input("...\n")
    if playerDifficulty == "3":
        print("DIFFICULTY: HARD")
        numGuesses = 3
    elif playerDifficulty == "2":
        print("DIFFICULTY: MEDIUM")
        numGuesses = 5
    else:
        print("DIFFICULTY: EASY")
        numGuesses = 10
    
    # GAME LOOP
    while numGuesses > 0:
        numGuesses -= 1
        attemptCount += 1
        guess = int(input("Guess a number:"))
        if guess == number:
            print(f"CORRECT {attemptCount}")
        elif guess > number:
            print(f"TOO HIGH\n{numGuesses} Guesses Left")
        elif guess < number:
            print(f"TOO LOW\n{numGuesses} Guesses Left")





if __name__ == "__main__":
    main()
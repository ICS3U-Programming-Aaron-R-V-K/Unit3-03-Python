# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: March 21, 2025
# The code is a guess random number game
# The code generates a random number, the user has to guess it
# The code will base his answer using an if else statement

import random


def main():
    # Generate the random number from 1 to 10
    random_number = random.randint(1, 10)
    # Get user guess as and integer
    guess_number = int(input("Guess a random number from 1 to 10: "))

    # If statement for the right answer
    if random_number == guess_number:
        print("Your are correct")
    # Else statement for any other answer that is not the correct number
    else:
        print("You are wrong, the correct answer was: {} ".format(random_number))


if __name__ == "__main__":
    main()

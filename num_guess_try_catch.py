#!/usr/bin/env python3
# Created By: Ishami Sebgoya
# Date: November 12, 2023
# This program asks the user if they guessed the correct random number
import random


def main():
    # Generate random number
    correct_number = random.randint(0, 9)

    try:
        user_input = input("Enter your guess: ")
        user_guess = int(user_input)

        if user_guess == correct_number:
            print("You guessed correctly.")
        else:
            print("Wrong guess.")
            print("The correct answer was:", correct_number)
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()


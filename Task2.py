"""
This code is used to create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The generate_random_number() function generates a random number between 1 and 100 and returns the same.

The validate_user_input() function checks if the input given by the user is between the range of 1-100 and returns
a True or False (boolean) value depending on the situation.

The print_result_message() takes the user_input and random_number as parameters and prints out the correct message.

The guess_random_number() function stores the main logic for the task. It takes user_input for the number
and generates a random number. It then validates the user_input and if it's a valid input, it checks
whether the user_input is higher, lower or equal to the random_number generated.

In the validate_user_input, we are "assuming" that the user_input is always going to be numeric, which need not
necessarily be true in the real world. To handle non-numeric user_inputs, other methods like checking the data type
of user_input can be checked and then the user_input can be validated. However, I have omitted that to keep the code
simple.
"""

# Importing the random library to generate a random number
import random


def generate_random_number():
    random_number = random.randint(1, 101)
    return random_number


def validate_user_input(user_input):
    if 1 <= user_input <= 100:
        return True
    else:
        return False


def print_result_message(user_input, random_number):
    if user_input < random_number:
        print("Guessed number is lower than the actual number")

    elif user_input > random_number:
        print("Guessed number is higher than the actual number")

    else:
        print("Correct guess!")


def guess_random_number():
    random_number = generate_random_number()
    user_input = int(input("Enter a number between 1 and 100: "))

    if validate_user_input(user_input):
        print_result_message(user_input, random_number)
    else:
        print("Invalid user input!")


guess_random_number()

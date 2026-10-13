# Name: Nam Pham
# Period: AM
# Guessing Gamme

import random
random_number = random.randrange(1, 10)
# This module from the python website library will, hopefully, return a random integer ranging from 1 to 10

previous_guesses = []
# This is where all of user's valid guesses will go and be stored without any repetition

user_guess = input("Enter a number from 1 to 10: ")
# Here is where user provides their first guess, stored inside of a variable that will change according to the code

while (int(user_guess) > 10) or (int(user_guess) < 1):
    print("Invalid guess!")
    user_guess = input("Enter a number from 1 to 10: ")
# This first validation check is to make sure the user's first guess is actually in the valid range

# This long while loop, containing while loops, will keep the game going and functioning properly without error
while (int(user_guess) == previous_guesses) or (int(user_guess) != random_number) or (int(user_guess) > 10 or int(user_guess) < 1):
    while (int(user_guess) > 10) or (int(user_guess) < 1):
        print("Invalid guess!")
        user_guess = input("Enter a number from 1 to 10: ")
    # This is to check again whether any of user's future guesses are in the correct range or not

    while int(user_guess) in previous_guesses:
        print("You have already guessed this number!")
        print("Previous guesses:", previous_guesses)
        user_guess = input("Enter a different number from 1 to 10: ")
    else:
        previous_guesses.append(int(user_guess))
    # Now here will determine if user has already guessed a number in the stored list yet and either adds it or rejects it

    if (int(user_guess) != previous_guesses) and int(user_guess) > random_number:
        print("Try again! The random number is lower.")
        print("Previous guesses:", previous_guesses)
        user_guess = input("Enter a different number from 1 to 10: ")
    else:
        print("Try again! The random number is higher.")
        print("Previous guesses:", previous_guesses)
        user_guess = input("Enter a different number from 1 to 10: ")
    # And these if/else statements tells the user whether their validated guess is lower or higher than the randomly generated number

print("Correct! You guessed the random number.")
# This will display once the user wins
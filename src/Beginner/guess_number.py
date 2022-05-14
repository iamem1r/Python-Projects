# Hi this the second mini project of beginner python

# Our gols is first choose a number as a limitation, then make a random number less than limited number.
# then we make a guess and we continue our guess to be equal to random number.

import random

limit_range = input("Please choose the top range of guessing game: ")

if limit_range.isdigit():
    limit_range = int(limit_range)

    if limit_range <= 0:
        print("Please choose a number greater than zero next time.")
        quit()
else:
    print("Please choose a number not text.")
    quit()

random_number = random.randint(0, limit_range)
guess = 0
while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Guess should be a number.")
        continue

    if user_guess > limit_range:
        print(f"You should pick a number less than {limit_range}")
    elif user_guess > limit_range:
        print(f"You should pick a number greater than {limit_range}")

    if user_guess == random_number:
        print("Yeaaaayyy, you made CORRECT guess!! Niiiice.")
        print(f"You made it in {guess} time.")
        break
    elif user_guess > random_number:
        print("Noooo, it's WRONG!")
        print("You are above the number.")
    elif user_guess < random_number:
        print("Noooo, it's WRONG!")
        print("You are below the number.")
        


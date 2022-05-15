# In this game we want to play with computer.
# we pick one thing from options and computer will generate for itself randomly.




import random

from sympy import Q


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Pick rock/paper/scissors or press q to quit: ").lower()

    if user_pick == "q":
        break

    elif user_pick not in options:
        print("Pick somthing valid.")
        continue

    rand_num = random.randint(0, 2)
    computer_pick = options[rand_num]

    if user_pick == "rock" and computer_pick == "scissors":
        print("Yeeayyyy, you WON!")
        print("Congrats...!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("Yeeayyyy, you WON!")
        print("Congrats...!")
        user_wins += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        print("Yeeayyyy, you WON!")
        print("Congrats...!")
        user_wins += 1
    else:
        print("Oh no, you LOST!!")
        print("Try again don't get disapointed!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("GoodBye!!!")
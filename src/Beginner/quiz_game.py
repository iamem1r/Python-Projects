# in this mini project we are going to ask some random questions from user,
# count the correct answers and finally print percentage of correct answers
import time


def sleep(sec=1):
    """it entrupts running code for N seconds.

    :param sec: Seconds to sleep, defaults to 1
    :type sec: int, optional
    """
    time.sleep(sec)

def quit_game():
    print("Oh no :( I wish to see you next time.")
    sleep(0.5)
    print("Bye Bye...")
    sleep()
    quit()


def continue_game():
    print("YooooHoooo!!")
    sleep(0.5)
    print("Let's play an exciting game!!")
    sleep(0.5)
    print("So, Let's Goooooo")
    print("- * -"* 20)


print("WELCOME to QUIZ game!!!!")
sleep()

playing = input("Do you want to play some Q/A game with me? " )
sleep()

if playing.lower() == 'yes':
    continue_game()
else:
    quit_game()


score = 0
answer = input("What is the capital of Brazil? ")
if answer.lower() == 'brasilia' or answer.lower() == 'brazilia':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

answer = input("What is the capital of Canada? ")
if answer.lower() == 'ottawa':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

answer = input("What is the capital of Cuba? ")
if answer.lower() == 'havana':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

answer = input("What is the capital of Egypt? ")
if answer.lower() == 'cairo':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

answer = input("What is the capital of Finland? ")
if answer.lower() == 'helsinki':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

answer = input("What is the capital of Germany? ")
if answer.lower() == 'berlin':
    print('Corrrrrect!')
    score += 1
else:
    print('Oooops! Incorrect...')

print(f"You answered {score} question right.")
sleep()
print(f"and your score percentage is {round((score/6*100), 0)}%")
sleep()

if score >= 5:
    print("Wow, you have a very good knowledge about countries.")
elif 2 < score < 4:
    print("You know countries well, but you should be more conscious!")
else:
    print("You should read more and more about countries.")



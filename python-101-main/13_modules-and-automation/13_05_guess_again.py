# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

count = 0
max_tries = 3
random_answer = random.randint(1,10)

while count < max_tries:
    guess = int(input("guess a number between 1 and 10: "))
    if guess == random_answer:
        print("you won the game!")
        break
    else:
        print("sorry thats not the right")
        count += 1
if count == max_tries:
    print("max tries exceeded")
        





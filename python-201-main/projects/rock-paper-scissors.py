# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
# rock beats scissor, scissor beats paper, paper beats rock

import random

options = ["rock", "paper", "scissors"]

user_input = int(input("enter a number 0-2: "))
computer_input = random.randint(0,2)

if user_input not in range(0,3):
    raise ValueError("you did not enter a valid number")

def get_hand(index: int) -> str:
    """take in an int from computer/user and 
    return string object from options"""
    return options[index]

def determine_winner(user, computer):
    if user == computer:
        print("This was a draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You are the winner!")
    else:
        print("Computer won!")

user_hand = get_hand(user_input)
print(f"User has selected {user_hand}")
computer_hand = get_hand(computer_input)
print(f"Computer has selected {computer_hand}")
determine_winner(user_hand, computer_hand)







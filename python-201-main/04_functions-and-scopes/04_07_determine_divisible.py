# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def divisible_by_four_or_seven(num):
    if num % 4 == 0 or num % 7 == 0:
        return True
    return False
    
def divisible_by_four_and_seven(num):
     if num % 4 == 0 and num % 7 == 0:
        return True
     return False

try:
    user_input = int(input("enter a number between 1 and 1,000,000,000: "))
    if 1 <= user_input <= 1000000000:
        print(f"is {user_input} divisible by four and seven? {divisible_by_four_and_seven(user_input)}")
        print(f"is {user_input} divisible by four or seven? {divisible_by_four_or_seven(user_input)}")
    else:
        print("number out of defined range")
except ValueError:
    print("invalid input type")
    

    

    

    
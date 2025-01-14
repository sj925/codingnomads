# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

health = 5
myset = set()
while health > 0:
    userinput = input("enter a number: ")
    if userinput.isdigit():
        if userinput in myset:
            print("this number is already in your set! that'll cost you 1 health")
            health -= 1
            if health == 0:
                print("sorry you ran out of health!")
        else:
            myset.add(userinput)
        if len(myset) > 10:
            print(f"you won the game as your set is greater than 10 numbers: {myset}")
            break
    else:
        print("you did not enter a number")
        break
   
    


    
    
    
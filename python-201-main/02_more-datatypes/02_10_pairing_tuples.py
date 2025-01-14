# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

# Write your code below here

lst = randlist
lst.sort()
print(lst)

new_lst = []

for num in range(0, len(lst), 2):
    if num + 1 < len(lst):
        pair = (lst[num], lst[num +1])
    else:
        pair = (lst[num], 0)
    new_lst.append(pair)
    print(pair)
    
print(new_lst)
        



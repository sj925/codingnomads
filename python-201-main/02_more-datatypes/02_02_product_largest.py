# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)

largest_number = max(randlist)
print(f'The largest number in the list is: {largest_number}')

product = 1 

for item in randlist:
    product *= item

print(f'the product of all the numbers in {randlist} =', product)
    




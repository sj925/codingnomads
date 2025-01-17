# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

user_string = input("Enter a string: ")

list_of_tuples = list(tuple(x) for x in user_string.split())

print(list_of_tuples)
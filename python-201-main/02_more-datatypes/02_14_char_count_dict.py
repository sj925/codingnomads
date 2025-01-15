# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

strng = input("enter a string: ")

mydict = {x: strng.count(x) for x in strng}
print(mydict)
# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

a = tuple(string)
print(a)
b = list(a)
print(b)
b[0] = "k"
b = tuple(b)
print(b)

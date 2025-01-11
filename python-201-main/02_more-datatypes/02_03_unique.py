# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

mylist = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
newlist =list(set(mylist))
print(newlist)

#using list comprehension

otherlist = [x for x in mylist if mylist.count(x) == 1]
print(otherlist)

# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

#first way 

list_ = list(set(list_))
print(list_)

#second way if first list above was not already modified to catch dupes. would need to comment out first approach for second to work
        
list2 = []

for num in list_:
    if num not in list2:
        list2.append(num)
    else: 
        print("num already in list!")
print(list2)


 
    
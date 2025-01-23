# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x, y):
    return x / y

my_num = add(5, subtract(5,4))
another_num = subtract(27, multiply(4, 3))
another_another_num = (divide(100, add(5,5)))

print(my_num, another_another_num, another_num)
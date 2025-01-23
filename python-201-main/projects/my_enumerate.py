# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable):
      index = 0
      for item in iterable:
            yield index, item
      index += 1
      

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']
    
for index, item in my_enumerate(courses):
      print(f"{index}: {item}")
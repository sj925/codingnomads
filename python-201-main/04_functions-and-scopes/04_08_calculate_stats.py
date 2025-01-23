# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(lst):
  # define the function here
  maximum = max(lst)
  minimum = min(lst)
  average = sum(lst) / len(lst)
  summation = sum(lst)
  string = f"the minimum of {lst} is {minimum}\n the maximum of {lst} is {maximum}\n the average of {lst} is {average}\n the sum of {lst} is {summation}"
  print(string)
  return string

# call the function below here
stats(example_list)

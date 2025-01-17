# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

from pathlib import Path

words = Path.cwd().joinpath("words.txt")
lst = []

with open(words, "r") as file:
    for word in file:
        lst.append(word.strip())

min_len = (len(min(lst, key=len)))
max_len = (len(max(lst, key=len)))
min_words = [ word for word in lst if len(word) == min_len]
max_words = [word for word in lst if len(word) == max_len]
print(len(lst))
print(min_words, max_words)
        
      
    

# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

words = Path.cwd().joinpath("words.txt")

with open(words, "r") as file:
    for word in file:
        if len(word.strip()) > 20:
            print(word.strip()) 
    
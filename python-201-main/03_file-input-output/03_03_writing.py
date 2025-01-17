# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path

words = Path.cwd().joinpath("words.txt")
reverse_words = Path.cwd().joinpath("words_reverse.txt")

with open(words, "r") as infile, open(reverse_words, "w") as outfile:
    lines = infile.readlines()
    reverse_lines = lines[::-1]
    outfile.writelines(reverse_lines)




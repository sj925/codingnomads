# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.


#instead of user input, mocked it. 
passage = (
    "The sun dipped below the horizon, painting the sky in hues of orange and pink. "
    "A gentle breeze rustled the leaves, carrying with it the promise of a calm evening. "
    "Somewhere in the distance, the faint sound of laughter echoed, a reminder of simpler times."
)

words = [word.strip('.,') for word in passage.split(" ")]
word_count = {x: words.count(x) for x in set(words)}
most_common = max(word_count, key=word_count.get)
count = word_count[most_common]

print(f'The most common word is "{most_common}" appearing {count} times')

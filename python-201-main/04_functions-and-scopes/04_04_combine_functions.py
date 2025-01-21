# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.


def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence


def write_letter(greeting, name, text):
    greeting_message = greet(greeting, name)
    letter_body = f"{text}"
    goodbye = f"Goodbye, {name}! Take care."
    return f"{greeting_message}\n\n{letter_body}\n\n{goodbye}"

print(write_letter("Hello", "Sean", "I hope this message finds you well."))

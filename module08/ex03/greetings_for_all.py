#!/opt/pyenv/shims/python

import sys

def greetings_for_all(string):
    return f"Hello, {string}!"

if len(sys.argv) != 2:
    print("Enter a string as an argument.")
    sys.exit(1)
    
user_input = sys.argv[1]

if not any(char.isalpha() for char in user_input):
    print("Error! It was not a name.")
    sys.exit(1)
print(greetings_for_all(user_input))

 
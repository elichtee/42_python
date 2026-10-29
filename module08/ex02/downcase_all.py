#!/opt/pyenv/shims/python

import sys

def downcase_all(string):
    return string.lower()

if len(sys.argv) != 2:
    print("Enter a string as an argument.")
    sys.exit(1)

user_input = sys.argv[1]

print(downcase_all(user_input))
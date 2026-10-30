#!/opt/pyenv/shims/python

import sys

def downcase_all(string):
    return string.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_all(arg))
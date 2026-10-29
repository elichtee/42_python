#!/opt/pyenv/shims/python

import sys

def shrink(string):
    return string[:8]

def enlarge(string):
    return string + "Z" * (8 - len(string))

if len(sys.argv) == 1:
    print("none")
    sys.exit(0)

for arg in sys.argv[1:]:
    if len(arg) < 8:
        print(enlarge(arg))
    elif len(arg) > 8:
        print(shrink(arg))
    else:
        print(arg)

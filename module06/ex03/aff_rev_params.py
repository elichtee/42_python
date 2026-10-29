#!/opt/pyenv/shims/python

import sys

arg = sys.argv[1:]

if len(arg) < 2:
	print("none")
else:
	for arg in reversed(sys.argv[1:]):
		print(arg)

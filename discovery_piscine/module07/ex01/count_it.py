#!/opt/pyenv/shims/python

import sys

#sys.argv contains script name + parameters
#Subtract 1 to get actual number of parameters passed.

n_parameters = len(sys.argv) - 1

if n_parameters == 0:
	print("none")
else:
	print(f"parameters: {n_parameters}")
	
	for i, arg in enumerate(sys.argv[1:], start=1):
		char_length = len(arg)
		print(f"{arg}: {char_length}")

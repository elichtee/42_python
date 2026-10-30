#!/opt/pyenv/shims/python

import sys

n_parameters = len(sys.argv) - 1

if n_parameters != 1:
	print("none")
else:
	input_string = sys.argv[1]
	z_count = input_string.count("z")
	
	if z_count == 0:
		print("none")
	else:
		for _ in range(z_count):
			print("z", end="")
		print()

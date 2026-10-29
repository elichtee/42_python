#!/opt/pyenv/shims/python

import sys

n_parameters = len(sys.argv) - 1

if n_parameters != 2:
	print("none")
else:
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])

	if n1 < n2:
		array = list(range(n1, n2 +1))
		print(array)
	else:
		print("none")

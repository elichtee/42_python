#!/opt/pyenv/shims/python

import math

try:
	n = float(input("Give me a number: "))
	
	if n.is_integer():
		print(f"{int(n)}")
	else:
		rounded_up = math.ceil(n)
		print(f"{rounded_up}")

except ValueError:
	print("Error: Please enter a valid number.")

#!/opt/pyenv/shims/python

try:
	n = float(input("Give me a number: "))

	if n.is_integer():
		print(f"This number is an integer.")
	else:
		print(f"This number is a decimal.")

except ValueError:
	print("Error: Please provide a valid number.")


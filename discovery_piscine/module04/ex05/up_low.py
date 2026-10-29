#!/opt/pyenv/shims/python

i = input("Enter a string: ")

if i.isdigit():
	print("Error: Please enter a string.")

else:
	print(i.swapcase())



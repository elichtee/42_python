#!/opt/pyenv/shims/python

numbers = [2, 8, 9, 48, 8, 22, -12, 2]

print (f"Original list: {numbers}")

for i,num in enumerate(numbers):
	numbers[i] = num + 2

print(f"New list: {numbers}")



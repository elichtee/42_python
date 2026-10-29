#!/opt/pyenv/shims/python

numbers = [2, 8, 9, 48, 8, 22, -12, 2]

print(numbers)

new_list = [num + 2 for num in numbers if num > 5]
unique_numbers = set(new_list)

print(sorted(unique_numbers))

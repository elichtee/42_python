#!/opt/pyenv/shims/python

age_str = input("Please tell me your age: ")
age_int = int(age_str)

#Add 10,20,30 years
try:
	age_int = int(age_str)
	plus_10 = age_int + 10
	plus_20 = age_int + 20
	plus_30 = age_int + 30

	print(f"You are currently {age_int}")
	print(f"In 10 years, you'll be {plus_10} years old.")
	print(f"In 20 years, you'll be {plus_20} years old.")
	print(f"In 30 years, you'll be {plus_30} years old.")

except ValueError:
	print("Error: Please enter a valid whole number.")


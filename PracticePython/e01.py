"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
from datetime import date

def get_name():
	try:
		name = str(input('Please enter your name: >'))
	except:
		print("Invalid Input")
		return get_name()
	return name

def get_age():
	try:
		age = int(input('Please enter your age: >'))
	except:
		print("Invalid input, enter a number")
		return get_age()
	return age

def calculate_year(age):
	year = date.today().year
	birthday = year - age
	year = birthday + 100
	return year

def main():
	name = get_name()
	age = get_age()
	year = calculate_year(age)
	print(f'{name}, you will be 100 in the year {year}')
	exit(0)

main()

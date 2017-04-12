#!/usr/bin/python

'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Example:

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1
'''

def checkio(numbers):
	value = 1
	while numbers > 0:
		number = numbers % 10
		if number != 0:
			value = value * number
		numbers = (numbers - number) // 10
	return value




print checkio(123405)
print checkio(999)
print checkio(1000)
print checkio(1111)
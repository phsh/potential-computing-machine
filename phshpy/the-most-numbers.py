#!/usr/bin/python
'''
You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. 
So we should check the result with 0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).

Example:

checkio(1, 2, 3) == 2
checkio(5, -5) == 10
checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
checkio() ==

'''
def checkio(*args):
	if len(args) > 0:
		max_value=max(args)
		min_value=min(args)
		return max_value-min_value
	else:
		return 0
    


def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision   

print(checkio(1, 2, 3))
print almost_equal(checkio(1, 2, 3), 2, 3)
print checkio(5, -5)
print almost_equal(checkio(5, -5), 10, 3)
print checkio(10.2, -2.2, 0, 1.1, 0.5)
print almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3)
print checkio()
print almost_equal(checkio(), 0, 3)
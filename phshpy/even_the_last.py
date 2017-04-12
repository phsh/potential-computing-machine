#!/usr/bin/python
'''
You are given an array of integers. 
You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 

then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

Example:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0


'''
def end_the_last(n_array):
	ret = 0
	last = 0
	if len(n_array) > 0 :
		for index, value in enumerate(n_array):
			last = value
			if index % 2 == 0 :				
				ret += value
		ret *= last
	return ret

print end_the_last([0, 1, 2, 3, 4, 5])
print end_the_last([1,3,5])
print end_the_last([6])
print end_the_last([])

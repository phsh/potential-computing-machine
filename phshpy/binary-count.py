#!/usr/bin/python
'''
For the Robots the decimal format is inconvenient. If they need to count to "1", 
their computer brains want to count it in the binary representation of that number. 
You can read more about binary here.

You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) 
are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.

Example:

checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

'''

def checkio(numbera):
	value = 0
	valueNumber = numbera
	while valueNumber > 0 :		
		value += valueNumber % 2
		valueNumber = valueNumber // 2
	return value



print checkio(4)
print checkio(15)
print checkio(1)
print checkio(1022)
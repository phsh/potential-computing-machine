#!/usr/bin/python
'''
Do you remember the radix and Numeral systems from math class? Let's practice with it.

You are given a positive number as a string along with the radix for it. Your function should convert it into decimal form. The radix is less than 37 and greater than 1. The task uses digits and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted. For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

Input: Two arguments. A number as string and a radix as an integer.

Output: The converted number as an integer.

Example:

checkio("AF", 16) == 175
checkio("101", 2) == 5
checkio("101", 5) == 26
checkio("Z", 36) == 35
checkio("AB", 10) == -1
    
'''
def checkio(strValue, radix):	
	value = 0
	numValue = 0;
	for i in reversed(range(0, len(strValue))):
		counter = (radix**(len(strValue)-1 - i))
		if  strValue[i].isalpha():			
			numValue = ord(strValue[i].lower()) - 96 + 9 											
		else:
			numValue = int(strValue[i])
		if numValue >= radix :
			return -1
		value = value +  numValue*counter			
	return value
print checkio("AF", 16)
print checkio("101", 2)
print checkio("101", 5)
print checkio("Z", 36)
print checkio("AB", 10)
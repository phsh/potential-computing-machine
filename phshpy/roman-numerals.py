#!/usr/bin/python
'''
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:

Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.

checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'
'''
def trans(num, one, five, ten):
	'''
	0 = ""
	1 = "I"
	2 = "II"
	3 = "III"
	4 = "IV"
	5 = "V"
	6 = "VI"
	7 = "VII"
	8 = "VIII"
	9 = "IX"
	'''
	value = ""
	if num > 0 and num < 4:
		for x in range(num):			
			value += one
	if num == 4:
		value = one + five
	if num > 4 and num < 9:
		value = five
		for x in range(5,num):			
			value += one
	if num == 9:
		value = one + ten			
	return value
	
		

def checkio(num):
	strValue=""
	one = num % 10
	ten = (num // 10 ) % 10
	hundred = (num // 100) % 10
	thousand = (num // 1000) % 10
	strValue += trans(thousand, "M", "M", "M")
	strValue += trans(hundred, "C", "D", "M")
	strValue += trans(ten, "X", "L", "C")
	strValue += trans(one, "I", "V", "X")
	return strValue


print checkio(6)
print checkio(76)
print checkio(13)
print checkio(44)
print checkio(3999)

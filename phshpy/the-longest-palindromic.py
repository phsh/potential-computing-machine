#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

Write a function that finds the longest palindromic substring of a given string. Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.

Precondition: 1 < |text| ≤ 20
The text contains only ASCII characters.


'''
def isPalindrom(text):
	if text[::-1] == text:
		return True
	return False

def longest_palindromic(text):	
	palindrom=""
	index = 0
	while index < len(text):
		palcheck=text[index:]
		pal_index=0
		while pal_index <= len(palcheck):
			if len(palcheck[:pal_index]) > 0:
				if isPalindrom(palcheck[:pal_index]):
					if len(palcheck[:pal_index]) > len(palindrom):
						palindrom = palcheck[:pal_index]					
			pal_index += 1
			
		index += 1
	
	return palindrom


print longest_palindromic("A")
print longest_palindromic("AA")
print longest_palindromic("ABA")
print longest_palindromic("ABBA")
print longest_palindromic("ABCBA")
print longest_palindromic("ABCDBA")
print longest_palindromic("rtrartr")
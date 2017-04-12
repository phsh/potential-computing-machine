#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Great!” Exclaimed Sofia. “Now we have the password.”

“To what exactly?” Quipped Nikola.

“Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart desires!”

“And you’re going to do what with a password to absolutely nothing?” Nikola smirked.

“Oh... Right...”

Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. 
We could try fixing it and then punching in the password?”

“YES! That!” Sofia exclaimed.

You are given an expression with numbers, brackets and operators. For this task only the brackets matter. 
Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. 
If a bracket is open, then it must be closed with a closing bracket of the same type. 
The scope of a bracket must not intersected by another bracket. 
In this task you should make a decision, whether to correct an expression or not based on the brackets. 
Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Example:

checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
checkio("2+3") == True
'''

def checkio(stringVariable):
	okay = False
	countA=0 #()
	countB=0 #{}
	countC=0 #[]
	openArray = list()

	for c in stringVariable:		
		if c == '(':						
			countA += 1
			openArray.append(c)
		if c == ')':
			if len(openArray) > 0  and openArray.pop() != '(':
				return False
			countA -= 1			
		if c == '{':
			countB += 1
			openArray.append(c)
		if c == '}':
			if len(openArray) > 0  and openArray.pop() != '{':
				return False
			countB -= 1
		if c == '[':
			countC += 1
			openArray.append(c)
		if c == ']':
			if len(openArray) > 0  and openArray.pop() != '[':
				return False
			countC -= 1			
	if countA == 0 and countB == 0 and countC == 0:
		okay = True 
	return okay


print checkio("((5+3)*2+1)")
print checkio("{[(3+1)+2]+}")
print checkio("(3+{1-1)}")
print checkio("[1+1]+(2*2)-{3/3}")
print checkio("(({[(((1)-2)+3)-3]/3}-3)")
print checkio("2+4")

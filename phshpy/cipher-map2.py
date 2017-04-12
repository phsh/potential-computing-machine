#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Help Sofia write a decrypter for the passwords that Nikola will encrypt through the cipher map. 
A cipher grille is a 4×4 square of paper with four windows cut out. 
Placing the grille on a paper sheet of the same size, 
the encoder writes down the first four symbols of his password inside the windows (see fig. below). 
After that, the encoder turns the grille 90 degrees clockwise. 
The symbols written earlier become hidden under the grille and clean paper appears inside the windows. 
The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. 
Then, they write down the following four symbols and turns the grille once more. 
Lastly, they write down the final four symbols of the password. 
Without the same cipher grille, it is difficult to discern the password from the resulting square comprised of 16 symbols. 
Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.



Write a module that enables the robots to easily recall their passwords through codes when they return home.

The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.

Output: The password as a string.

Example:

recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'ican tfor geti ddqd'
​
recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqr wsfz xqxz hczy'
'''
def findChars(grilleMatrix, textMatrix):
	returnText=""
	rowCount=0
	
	while rowCount < len(grilleMatrix):
		elmentCount = 0		
		while elmentCount < len(grilleMatrix[rowCount]):
			if grilleMatrix[rowCount][elmentCount] == 'X':
				returnText += textMatrix[rowCount][elmentCount]
			elmentCount += 1
		rowCount += 1
	return returnText

def recall_password(grille, password):
	grilleMatrix = [[0 for x in range(4)] for y in range(4)]
	textMatrix = [[0 for x in range(4)] for y in range(4)]
	text = ""
	rowCount=0
	for row  in grille:
		elmentCount = 0
		for elment in row:
			grilleMatrix[rowCount][elmentCount]=elment
			elmentCount += 1
		rowCount += 1
	rowCount=0	
	for row  in password:
		elmentCount = 0
		for elment in row:
			textMatrix[rowCount][elmentCount]=elment
			elmentCount += 1
		rowCount += 1
	turns = 0
	while turns < 4:
		text += findChars(grilleMatrix, textMatrix)
		grilleMatrix= zip(*grilleMatrix[::-1])
		turns += 1
	return text

print recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr'))


print recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi'))
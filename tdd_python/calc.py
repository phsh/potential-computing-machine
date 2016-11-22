#!/usr/bin/env python
import sys
import fileinput
from app.calculator import Calculator

calcu = Calculator()
firstNumber = 0
secondNumber = 2
command = 1
tripleCommand = []
for compleatLine in fileinput.input():
	for commandParts in compleatLine.rstrip().split():
		tripleCommand.append(commandParts)
result = "'" + str(tripleCommand[command]) + "' no such method supported. \n" + str(calcu.legal())
print tripleCommand
if tripleCommand[command] in calcu.legal():
	result = getattr( calcu,tripleCommand[command])(int(tripleCommand[firstNumber]), int(tripleCommand[secondNumber]) )
print result
#!/usr/bin/env python
import sys
import fileinput
from app.calculator import Calculator

calcu = Calculator()
lista = []
for line in fileinput.input():
	for lineParts in line.rstrip().split():
		lista.append(lineParts)
result = "'" + str(lista[1]) + "' no such method supported. \n" + str(calcu.legal())
print lista
if lista[1] in calcu.legal():
	result = getattr(calcu,lista[1])(int(lista[0]), int(lista[2]) )	

print result
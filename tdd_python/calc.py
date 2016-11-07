#!/usr/bin/env python
import sys
import fileinput
from app.calculator import Calculator

calcu = Calculator()
lista = []
for line in fileinput.input():
    lista.append(line.rstrip())
result = "'" + str(lista[1]) + "' no such method supported. \n" + str(calcu.legal())
if lista[1] in calcu.legal():
	result = getattr(calcu,list[1])(int(list[0]), int(list[2]) )
print lista
print result
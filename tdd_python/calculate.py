#!/usr/bin/env python
import sys
from app.calculator import Calculator

calc = Calculator()
lista = sys.argv
result = "'" + str(sys.argv[2]) + "' no such method supported. \n" + str(calc.legal())
if sys.argv[2] in calc.legal():
	modifier = sys.argv[2]
	if len( sys.argv[2] ) == 1:
		modifier = calc.character(sys.argv[2])		
	result = getattr(calc,modifier)(int(sys.argv[1]), int(sys.argv[3]) )
print result
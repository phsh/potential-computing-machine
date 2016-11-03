#!/usr/bin/env python
import sys
from app.calculator import Calculator

calc = Calculator()
lista = sys.argv
result = "'" + str(sys.argv[2]) + "' no such method supported. \n" + str(calc.legal())
if sys.argv[2] in calc.legal():
	result = getattr(calc,sys.argv[2])(int(sys.argv[1]), int(sys.argv[3]) )
print result
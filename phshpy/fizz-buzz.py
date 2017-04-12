#!/usr/bin/python

def checkio( number ):
	ret = str(number)
	if number % 5 == 0:
		ret = "Buzz"
	if number % 3 == 0:
		ret = "Fizz"
	if number % 15 == 0:
		ret = "Fizz Buzz"
	return ret

print checkio(15)
print checkio(6)
print checkio(5)
print checkio(7)

# "Fizz Buzz" if the number is divisible by 3 and by 5;
# "Fizz" if the number is divisible by 3;
# "Buzz" if the number is divisible by 5; 
# The number as a string for other cases.
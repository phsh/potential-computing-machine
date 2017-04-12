#!/usr/bin/python

'''
How old are you in number of days? It's easy to calculate - just subtract your birthday from today. We could make this a real challenge though and count the difference between any dates.

You are given two dates as tuples with three numbers - year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about absolute value.

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

Example:

days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238
days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    
1
2
3
4
How it is used: Python has batteries included, so in this mission you will need to learn how to use completed modules so that you don't have to invent the bicycle all over again.

Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.

'''
import datetime

def days_diff(start_date,end_date):
	start_datetime=datetime.date(*start_date)
	end_datetime=datetime.date(*end_date)	
	return abs((start_datetime-end_datetime).days)

print (days_diff((1982, 4, 19), (1982, 4, 22)))
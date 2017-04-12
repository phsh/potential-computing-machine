#!/usr/bin/python

'''

The island has eight stations which are connected by a network of teleports; 

however, the teleports take a very long time to recharge. 

This means you can only use each one once. 

After you use a teleport, it will shut down and no longer function. 

But you can visit any station more than once. 

For this task, you should begin at number 1 and try to travel around to all the stations before returning to the starting point. 

The map of the teleports is presented as a string in which the comma-separated list represents teleports. 

Each teleport is given the name of the station it connects to. 

This name consists of two digits, such as '12' or '32.' 

Each test requires you to provide a route which passes through every station. 

A route is presented as a string of the station numbers in the sequence in which they must be visited (ex. 123456781).

'''
def checkio(travel):
	path="123456781"
	options = travel.split(",")  	
	for option in options:
		for k,v in option:
			print k + v

	return path


print checkio("12,23,34,45,56,67,78,81")
#print checkio("12,28,87,71,13,14,34,35,45,46,63,65")
#print checkio("12,15,16,23,24,28,83,85,86,87,71,74,56")
#print checkio("13,14,23,25,34,35,47,56,58,76,68")
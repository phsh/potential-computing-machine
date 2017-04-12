#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
For the mission "How to find friends" , it’s nice to have access to a specially made data structure. In this mission we will realize a data structure which we will use to store and work with a friend network.

The class "Friends" should contains names and the connections between them. 
Names are represented as strings and are case sensitive. 
Connections are undirected, so if "sophia" is connected with "nikola", then it's also correct in reverse.

class Friends(connections)

Returns a new Friends instance. "connections" is an iterable of sets with two elements in each. Each connection contains two names as strings. Connections can be repeated in the initial data, but inside it's stored once. Each connection has only two states - existing or not.

>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
>>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)

Add a connection in the instance. "connection" is a set of two names (strings). Returns True if this connection is new. Returns False if this connection exists already.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.add({"1", "3"})
False
>>> f.add({"4", "5"})
True

remove(connection)

Remove a connection from the instance. "connection" is a set of two names (strings). Returns True if this connection exists. Returns False if this connection is not in the instance.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.remove({"1", "3"})
True
>>> f.remove({"4", "5"})
False

names()

Returns a set of names. The set contains only names which are connected with somebody.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
>>> f.names()
{"a", "b", "c", "d"}
>>> f.remove({"d", "c"})
True
>>> f.names()
{"a", "b", "c"}

connected(name)

Returns a set of names which is connected with the given "name". If "name" does not exist in the instance, then return an empty set.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
>>> f.connected("a")
{"b", "c"}
>>> f.connected("d")
set()
>>> f.remove({"c", "a"})
True
>>> f.connected("c")
{"b"}
>>> f.remove({"c", "b"})
True
>>> f.connected("c")
set()

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Friends class.

Output: The behaviour as described.

How it is used: Here you will implement a class with mutable states. 
This is not a simple structure with a couple of functions, but object representation with more complex structure.

Precondition: All data is correct.
'''
class Friends:
	connections = set()

	def __init__(self, connections):
		self.connections = list(connections)

	def haveConnection(self,connection,remove=False):
		key = connection.pop()
		value = connection.pop()
		found=False
		for pair in self.connections:   			
			if key in pair and value in pair:
				found=True
				if remove:
					remove_list=[key,value]
					self.connections.remove(set(remove_list))
					pass
		return found
	def add(self,connection):   		
		connectionCopy = list(connection.copy())
		found=self.haveConnection(connection)
		if not found :
			self.connections.append(set(connectionCopy))
		return not found

	def printa(self):
		print(self.connections)

	def remove(self,connetion):   		
		found=self.haveConnection(connetion,True)
		return found

	def names(self):
		names=set()
		tmp_names=list()
		print str(self.connections)
		connectionCopy = self.connections
		for pair in self.connections:
			pair_copy = pair.copy()
			tmp_names.append(pair_copy.pop())
			tmp_names.append(pair_copy.pop())   		
		return set(tmp_names)

	def connected(self,name):
		connections = set()
		for pair in self.connections:
			if name in pair:
				pair_copy = pair.copy()
				temp_list=list()
				temp_list.append(pair_copy.pop())
				temp_list.append(pair_copy.pop())
				for entry in temp_list:
					if not (entry == name):
						connections.add(entry)
		return connections
f=Friends([{"1", "2"}, {"3", "1"}])
print "add"
print f.add({"1", "3"})
print f.add({"2", "3"})
f.printa()
print "remove"
print f.remove({"1", "3"})
print f.remove({"4", "5"})
print "names"
print f.names()
print "connected(name)"
print f.connected("1")
f.printa()

print "some missing test"
f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
print "remove " + str(f.remove({"stephen", "robot"}))
print "names = " + str(f.names())
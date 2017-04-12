#!/usr/bin/python
'''
Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. 
You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

'''
def find_message(three_words):	
	found = three_words[0].isalpha() and three_words[1].isalpha() and three_words[2].isalpha()
	return found

def words(string_of_words):
	list_of_words = string_of_words.split()
	index = 0
	found = False	
	while index < (len( list_of_words ) - 2) and found == False:
		found  = find_message( list_of_words[ index : index + 3 ] )
		index = index + 1
	return found


print words("Hello World hello")
print words("He is 123 man")
print words("1 2 3 4")
print words("bla bla bla bla")
print words("Hi")
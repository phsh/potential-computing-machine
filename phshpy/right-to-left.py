#!/usr/bin/python
'''
One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

Input: A sequence of strings as a tuple of strings (unicode).

Output: The text as a string.

Example:

left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"
    
1
2
3
4
5
How it is used: This is a simple example of operations using strings and sequences.

Precondition:
0 < len(phrases) < 42
'''

def left_join(phrases):	
	words = [w.replace('right', 'left') for w in phrases]    
	return ",".join(words)


    
print left_join(("left", "right", "left", "stop"))
print left_join(("bright aright", "ok"))
print left_join(("brightness wright",))
print left_join(("enough", "jokes"))
print left_join(("right","leftrightleft","rightrightright"))
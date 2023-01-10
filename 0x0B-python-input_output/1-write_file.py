#!/usr/bini/python3
"""
Written a string to a text file and returns the number of characters written
"""

def write_file(filename= "", text=""):
 
"""
	Write a string to a UTF8 text file
	
	Args:
	filename - the name of the file to write
	text - the text to be writtem
	
	Returns - The number of characters written
"""
	with open(filename, "w" , encoding= "utf-8") as f:
		return f.write(text)


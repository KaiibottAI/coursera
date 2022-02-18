#!/usr/bin/env python3

def character_frequency(filename):
	""" Counts the frequency of each character in ghte given file. """
	#First try to open the file
	try:
		f = open(filename)
	except OSError:
		return None

	#ow process the file
	characters = {}
	for line in f:
			for char in line: 
				characters[char] = character.get(cher, 0) + 1
	f.close()
	return characters
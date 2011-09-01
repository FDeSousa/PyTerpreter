"""	PyFuck - Brainfuck Interpreter in Python

	This module is the interpreter class itself, which can
	be covered by an interface for usefulness or to aide in
	expanding the program to interpret more languages later
"""

__author__ = "Filipe De Sousa (filipe@desousa.com.pt)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/08/28 11:42:20 $"
__copyright__ = "Copyright (c) 2011 Filipe De Sousa"
__license__ = "Python"

import os, sys, re, types

class Interpreter():
	"""	The interpreter class itself, which has the methods
		for doing all of the heavy lifting
	"""
	
	def __init__(self, tointerpret):
		"Initialize program with the parsed-in program string"
		# Make a copy of the string to interpret while first replacing
		# digits/whitespace/word characters with nothing
		program = re.sub('[\d\s\w]', '', tointerpret.lower())
		# Initialise a pointer to 0 before starting interpreter
		pointer = 0
		# Set our numbers array to all zeroes, thirty thousand times
		arr = [0] * 30000
		
	def run(self):
		"The main run loop for the interpreter"
		# Should go through the program string and decide what
		# to do per-character
		# Maybe use RegEx to remove all the white space characters?
		for c in program:
			if c == '<':
				if pointer > 0:
					pointer -= 1
			elif c == '>':
				if pointer < len(arr)-1:
					pointer += 1
			elif c == '+':
				arr[pointer] += 1
			elif c == '-':
				arr[pointer] -= 1
			elif c == '[':
				# If current pointer is >= 1, enter loop
			elif c == ']':
				# If current pointer is >= 1, return into loop
			elif c == '.':
				# Print char representation of arr[pointer]
			elif c == ',':
				# Get one char from keyboard into arr[pointer]
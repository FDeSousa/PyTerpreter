"""	PyFuck - Brainfuck Interpreter in Python

	This module is the interpreter class itself, which can
	be covered by an interface for usefulness or to aide in
	expanding the program to interpret more languages later
"""

__author__ = "Filipe De Sousa (filipe@desousa.com.pt)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/09/03 21:16:20 $"
__copyright__ = "Copyright (c) 2011 Filipe De Sousa"
__license__ = "Python"

import os, sys, re, types
from PyTerpreter import Interpreter, Menu

# The PyFuck menu class, to be created and instantiated when
class PyMenuFucker(Menu):
	"""	The interpreter's menu class, which displays and works
		on the selected options
	"""	
	def __init__(self):
		"Only initialises the super class currently"
		Menu.__init__(self)
	
	def menu(self):
		"Handle the menu options the user has for PyFuck"
		run_menu = True
		
		while run_menu:
			# Display a menu here once per time the loop runs
			print "%2d. %s" % (1, "Interactive Interpreter")
			print "%2d. %s" % (2, "Run from file")
			print "------------------------------"
			print "%2d. %s" % (0, "Exit PyFuck")
			print
			print "Enter option number:\t"
			# read what was entered here
			option = sys.stdin.readline()
			
			if option == '1':	# Run the interactive interpreter
				interactive()
			elif option == '2':	# Run a program from file
				runfromfile()
			elif option == '0':	# Exit this interpreter, back to main menu
				run_menu = False
				return None
			else:				# Unrecognised option, print simple error
				print "Invalid option, numbers only"
			# Must look at exceptions, and how to handle them
			
			# Add an extra empty line to clean up the output a bit
			print
	
	def run_interpreter(self, tointerpret):
		"Method to instantiate and run the interpreter"
		interpret = PyFucker(tointerpret)
		interpret.run()

# The PyFuck interpreter class, to be created and instantiated per program
class PyFucker(Interpreter):
	"""	The interpreter class itself, which has the methods
		for doing all of the heavy lifting
	"""	
	
	def __init__(self, tointerpret):
		"Initialize program with the parsed-in program string"
		# Initialise the super class
		Interpreter.__init__(self, tointerpret)
		# Make a copy of the string to interpret while first replacing
		# digits/whitespace/word characters with nothing
		program = re.sub('[\d\s\w]', '', tointerpret.lower())
		# Initialise a pointer to 0 before starting interpreter
		pointer = 0
		# Set our numbers array to all zeroes, thirty thousand times
		arr = [0] * 30000
	
	def run(self):
		"The main run loop for the interpreter"
		# Run the super class run() method first off
		Interpreter.run(self)
		# Should go through the program string and decide what
		# to do per-character
		# Maybe use RegEx to remove all the white space characters?
		# To allow iterating backwards through the string, we're
		# using i to hold the index in the string
		i = 0
		while i < len(self.program):
			if c == '<':
				if self.pointer > 0:
					self.pointer -= 1
					i += 1
			elif c == '>':
				if self.pointer < len(self.arr)-1:
					self.pointer += 1
					i += 1
			elif c == '+':
				self.arr[self.pointer] += 1
				i += 1
			elif c == '-':
				self.arr[self.pointer] -= 1
				i += 1
			elif c == '[':
				# If current pointer is >= 1, enter loop
			elif c == ']':
				# If current pointer is >= 1, return into loop
			elif c == '.':
				# Print char representation of arr[pointer]
				i += 1
			elif c == ',':
				# Get one char from keyboard into arr[pointer]
				i += 1
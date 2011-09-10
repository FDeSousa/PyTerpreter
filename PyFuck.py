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
	
	# Since Python has no switch..case statement, using dictionary
	# to execute a function depending upon the current command
	# Inspiration came from: http://bytebaker.com/2008/11/03/switch-case-statement-in-python/
	commands = {'<' : dec_pointer,
				'>' : inc_pointer,
				'+' : inc_data,
				'-' : dec_data,
				'[' : loop_start,
				']' : loop_end,
				'.' : print_char,
				',' : read_char
	}
	
	def __init__(self, tointerpret):
		"Initialize program with the parsed-in program string"
		# Initialise the super class
		Interpreter.__init__(self, tointerpret)
		# Make a copy of the string to interpret while first replacing
		# digits/whitespace/word characters with nothing
		program = re.sub('[\d\s\w]', '', tointerpret.lower())
	
	def run(self):
		"The main run loop for the interpreter"
		# Run the super class run() method first off
		Interpreter.run(self)
		
		# The pointer and data array are unique to the run-time, so
		# initialise a pointer to 0 before starting interpreter:
		pointer = 0
		# and set our numbers array to all zeroes, 30,000 times over:
		arr = [0] * 30000
		
		# Should go through the program string and decide what
		# to do per-character
		# To allow iterating backwards through the string, we're
		# using i to hold the index in the string
		i = 0
		while i < len(self.program):
			# Hold the current char/command to execute in c
			c = self.program[i]
			
			try:
				# Try to execute the command here
				commands[c](self, pointer, arr, i)
			except KeyError:
				# If the command isn't found, dictionary will raise a
				# KeyError exception as the command is the key
				# We don't much mind, just ignore the key and carry on!
				pass
	
	def dec_pointer(self, pointer, arr, i):
		"Decrement the program pointer"
		# Function for the '<' command
		
		# Only decrement the pointer if it's more than 0
		if pointer > 0:
			pointer -= 1
			i += 1
	
	def inc_pointer(self, pointer, arr, i):
		"Increment the program pointer"
		# Function for the '>' command
		
		# Only increment the pointer if it's less than arr's length
		if pointer < len(arr)-1:
			pointer += 1
			i += 1
	
	def inc_data(self, pointer, arr, i):
		"Increment the data value in arr[pointer]"
		# Function for the '+' command
		
		# No conditional here, just increment the data at arr[pointer]
		arr[pointer] += 1
		i += 1
	
	def dec_data(self, pointer, arr, i):
		"Decrement the data value in arr[pointer]"
		# Function for the '-' command
		
		# No conditional here, just decrement the data at arr[pointer]
		arr[pointer] -= 1
		i += 1
	
	def loop_start(self, pointer, arr, i):
		"Check for loop start condition, start if possible"
		# Function for the '[' command
		
		# If data at arr[pointer] is >= 1, enter loop
		# Until I figure out how I want to do this, have just a pass
		pass
	
	def loop_end(self, pointer, arr, i):
		"Check for loop end condition, restart if possible"
		# Function for the ']' command
		
		# If data at arr[pointer] is >= 1, return into loop
		# Until I figure out how I want to do this, have just a pass
		pass
	
	def print_char(self, pointer, arr, i):
		"Print the char representating the data in arr[pointer]"
		# Function for the '.' command
		
		# Print char representation of arr[pointer]
		print chr(arr[pointer])
		i += 1
	
	def read_char(self, pointer, arr, i):
		"Read one char's associated value into arr[pointer]"
		# Function for the ',' command
		
		# Currently only reads one char at a time, and only after
		# pressing return/enter. To get rid of the '\n' from the
		# .read() buffer, we do another .read(1)
		# Must find a way to read just the one byte...
		
		# Get one char from keyboard into char_in
		char_in = ord(sys.stdin.read(1))
		# To make sure we don't get a '\n' next time, read another
		sys.stdin.read(1)
		# Now place char_in into arr[pointer]
		arr[pointer] = char_in
		i += 1



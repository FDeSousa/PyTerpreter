"""	PyTerpreter - Interpreter Interface in Python

	This module is the interface to the interpreter, and
	handles the input and output of the program as a whole
"""

__author__ = "Filipe De Sousa (filipe@desousa.com.pt)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/09/03 21:16:20 $"
__copyright__ = "Copyright (c) 2011 Filipe De Sousa"
__license__ = "Python"

import os, sys, types
import PyFuck

menu = {
	0:"Exit", 1:"PyFuck", 8:"-"
}
separator = "------------------------------"

def showmenu():
	runmenu = True
	
	while runmenu:
		for i in range(1,10):
			if menu.has_key(i):
				if menu[i] != "-":
					print "%2d. %s" % (i, menu[i])
				else:
					print separator
			# If the key doesn't exist, just skip over that number
		# After printing options 1-9, print the 0 option, Exit
		print "%2d.%s" % (0, menu[0])
		
		# Now get the option the user chose
		option = sys.stdin.readline()
		if option == '0':
			# Exit on option 0, it's associated with "Exit"
			runmenu = False
			return None
		elif menu[option] == '-':
			# Pass over this option, it's a filler
			pass
		elif !menu.has_key[option]:
			# Tell the user this option is invalid
			print "Invalid menu option entered"
		else:
			if option == '1':
				PyFuck.menu()
		
		# Clean up output, add an extra clear line
		print

class Menu():
	"""	Inheritable menu class for the language interpreter
	"""	
	
	def __init__(self):
		"Initialise run_menu to True"
		run_menu = True
	
	def menu(self):
		"Method to run the menu system, here toggles run_menu"
		if self.run_menu:
			self.run_menu = False
		else:
			self.run_menu = True
	
	def interactive(self):
		"Runs the interpreter interactively, line-by-line"
		# Show the message once, loop to get lines of program code
		print "Write a program per line to run, 'QUIT' to quit"
		run_interactive = True
		
		while run_interactive:
			user_input = sys.stdin.readline()
		
			if user_input == 'QUIT':
				# Quit the program here
				run_interactive = False
				return None
			else:
				# Parse the entered program to the Interpreter class
				self.run_interpreter(self, tointerpret)
	
	def run_from_file(self):
		"Runs a program loaded from a file"
		# Have yet to add file reading code/capabilities, must add
		# Load the named file, prompt when to run the program
		print "Enter program file name:\t"
		filename = sys.stdin.readline()
		
	def run_interpreter(self, tointerpret):
		"Overridable method for running the specific interpreter"
		# Does nothing, it's here to force the sub-class to use it
		pass

class Interpreter():
	"""	The inheritable interpreter class itself, which has
		the methods for doing all of the heavy lifting
	"""
	
	def __init__(self, tointerpret):
		"Initialises program_to_interpret, as a copy of the
		 original program parsed in"
		# program_to_interpret is just a copy of the original program
		program_to_interpret = tointerpret
	
	def run(self):
		"Run method for the class"
		pass

# Runs when running the module on its own
if __name__ == "__main__":
	# If the module is executed, just show the menu, simple as
	showmenu()
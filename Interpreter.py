"""	PyFuck - Brainfuck Interpreter in Python

	This module is the interface to the interpreter, and
	handles the input and output of the program as a whole
"""

__author__ = "Filipe De Sousa (filipe@desousa.com.pt)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/08/28 11:42:20 $"
__copyright__ = "Copyright (c) 2011 Filipe De Sousa"
__license__ = "Python"

import os, sys, types
from Interpreter import Interpreter

def showmenu():
	"Show the menu for pyfuck"
	runmenu = True
	
	while runmenu:
		# Display a menu here once per time the loop runs
		# Options:
		# 1.	Interactive interpreter
		# 2.	Load text file
		# --------------------
		# 0.	Exit pyfuck
		# 
		# Enter option number:	_
		print "1.\tInteractive interpreter"
		print "2.\tRun from file"
		print "--------------------"
		print "0.\tExit PyFuck"
		print
		print "Enter option number:\t"
		# read what was entered here
		option = sys.stdin.readline()
		
		if option == '1':
			interactive()
		elif option == '2':
			runfromfile()
		elif option == '0':
			runmenu = False
			return None
		else:
			print "Invalid option, numbers only"
		
		print
		
def interactive():
	"Interprets the parsed-in program string"
	if type(program) == types.StringType:
		pass
		# if the program argument is a string, interpret it
	else:
		print "Need a string to interpret"
		
		# warn someone that a string is needed
	# interpret(program) function
	
def runfromfile():
	""
	pass

# Runs when running the module on its own
if __name__ == "__main__":
	# If the module is executed, just show the menu, simple as
	showmenu()
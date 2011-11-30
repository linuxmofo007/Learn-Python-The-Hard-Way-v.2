#!/usr/local/bin/python

# import modules
from sys import argv

# assign variables to script input variables
script, filename = argv

# Print some stuff to stdout
print "We are going to erase %r." % filename
print "If you don't want that to happen, hit CTRL-C (^C)."
print "If you do want this, hit RETURN."

# Get input to continue or stop
raw_input("?")

# Open the file that we specified as $filename
print "Opening the file..."
target = open(filename, 'w')

# Not too sure what truncating is all about yet
print "Truncating the file. Goodbye!"
target.truncate()

# Prompt for 3 lines of input
print "Now I am going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Write lines of input to $filename
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close the file
print "And finally, we close it."
target.close()

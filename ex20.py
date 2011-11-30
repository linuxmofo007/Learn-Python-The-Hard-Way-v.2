#!/usr/local/bin/python

# import modules
from sys import argv

# define variables for our script inputs
script, input_file = argv

# function to print entire contents of a file
def print_all(f):
  print f.read()

# function to put the open file postion back to the 'top'
def rewind(f):
  f.seek(0)

# print a specific line out of a file
def print_a_line(line_count, f):
  print line_count, f.readline()

# open a file specified on the script input
current_file = open(input_file)

# print the entire file to stdout
print "First let's print the whole file:\n"
print_all(current_file)

# bring us back to postion 0 on the opened file
print "Now let's rewind, kind of like a tape."
rewind(current_file)

# print the first 3 lines of this file
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1 
print_a_line(current_line, current_file)

#!/usr/local/bin/python

# declare variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print some variables
print x
print y

# print with some variable replacment 
print "I said %r." % x
print "I also said: '%s'." % y

# declare some variables 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print the above 2 vairables 
print joke_evaluation % hilarious

# declare some variables
w = "This is the left side of..."
e = "a string with a right side."

# concatenate the 2 variables together
print w + e

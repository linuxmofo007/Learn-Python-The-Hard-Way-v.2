#!/usr/local/bin/python

# modules to load
from sys import argv

# var names for argv module
script, user_name = argv
prompt = '> '

# display some input variables from run time and get user input
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

# print out info we have thus far collected
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Very nice.
""" % ( likes, lives, computer )

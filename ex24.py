#!/usr/local/bin/python

# print statements showing escapes and quotes
print "Let's practice everything"
print 'You\d need to know \'bout escapes \\ that do \n newlines and \t tabs.'

# triple quotes string tied to a variable
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehand passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""

# print statement
print "-------------"
print poem
print "-------------"

# print statement displaying answer
five = 10 -2 + 3 - 6
print "This should be five: %s" % five

# function to calculate 'inventory', returns the value of jelly beans, jars, and crates
def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates

# the amount of beans we start with
start_point = 10000
# catch the output of secret_formula() into beans, jars, crates
beans, jars, crates = secret_formula(start_point)

# print statements with variable replacement
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

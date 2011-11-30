#!/usr/local/bin/python

#
# Define some functions
# 

# add 2 numbers
def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b

# subtract 2 numbers
def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b

# multiply 2 numbers
def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b

# divide 2 numbers
def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b

# my test
def my_function(a, b, c):
  print "I have these inputs: %r | %r | %r" % (a, b, c)
  return a + b + c

# print statement
print "Let's do some math with just fractions!"

# Lets make some data
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# print statement with the values of the above variables
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# EC
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do this by hand?"

# my test
test = my_function(1, 2, 3)
print test

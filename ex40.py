#!/usr/local/bin/python

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
"""This guy takes the input, and looks for the value of the state and prints it out if it exists. If it doesn't it prints out that it can't be found"""
  if state in themap:
    return themap[state]
  else:
    return "Not found."

# assign the function to a variable
cities['_find'] = find_city

# True always returns true...
while True:
  # print out a prompt and get user input
  print "State? (ENTER to quit)",
  state = raw_input("> ")

  # break out of this loop if we don't enter anything (press enter to quit)
  if not state: break

  # if we haven't broken out yet...

  # assign a new variable and get 
  city_found = cities['_find'](cities, state)
  print city_found

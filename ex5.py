#!/usr/local/bin/python

# set some variables
my_name = 'Linux Mofo'
my_age = 30
my_height = 72
my_weight = 235
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

# Print out variables with some formatting
print "Let's talk about %s." % my_name
print "He's %r inches tall." % my_height
print "He's %r pounds heavy." % my_weight
print "Actually that's not too bad."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %r, %r, and %r I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# convert inches & pounds to centimeters and kilos
inches = 10
centimeters = 100
pounds = 10
kilos = 100

print "If I have", pounds, "lbs, it would equal", pounds / 2.2, "kilos."
print "If I have", kilos, "kilos, it would equal", kilos * 2.2, "pounds."
print "If I have", inches, "inches, it would equal", inches * 2.54, "centimeters."
print "If I have", centimeters, "centimeters, it would equal", centimeters * 0.39, "inches."

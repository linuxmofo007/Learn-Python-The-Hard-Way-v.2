#!/usr/local/bin/python

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

slim_cat = '''
He said "fuck you".
but then I said "piss off".
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print slim_cat

# EC
x = "I\"m awesome. Nar!"

print "%r" % x
print "%s" % x

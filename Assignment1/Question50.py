'''
Discrete Mathematics and Its Applications - Kenneth H. Rosen
MATH 2305 - Saint Mary's University
Assignment 1 - 6.1 - Exercise 50

How many bit strings of length 10 contain either five consecutive 0s or five consecutive 1s?
'''

from itertools import product # for generating all cases
import re # for regex

# Step 1
# Generate all binary strings of length 10

# variable to test with other lengths
stringLength = 10

# generate all possible string combinations
allCases =(["".join(seq) for seq in product("01", repeat=stringLength)])

print("All Cases: %i \n\n %s" % (len(allCases), allCases))


# Step 2
# Remove all entries that don't contain 00000 or 11111

# Regex pattern stating:
# any number of leading 0 or 1s
# 5*1 or 5*0
# any number of trailing 0 or 1s
pattern = re.compile("^[01]*(([1]{5})|([0]{5}))[01]*$")

# Create a new list that filters based on regex pattern
goodCases = filter(pattern.match, allCases)

print("\n\nGood Cases: %i \n\n %s" % (len(goodCases), goodCases))
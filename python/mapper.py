#!/usr/bin/env python
import sys
import string

# Input is in the form of strings, one per line for documents in input folder
for line in sys.stdin:
        # Remove whitespace
        line = line.strip().translate(string.maketrans("",""), string.punctuation)
        # For each word in the lin
        for word in line.split():
                # Print to stdout the k/v pairs that will be input to the 
                # reducer in tab delimited format
                print '%s\t%s' % (word, 1)



#!/usr/bin/env python
from operator import itemgetter
import sys

current = None
word = None
current_count = 0

# Get output of mapper from stdin
for line in sys.stdin:
        # Clean whitespace
        line = line.strip()
        # parse line, which should be of form word\tcount
        word, count = line.split('\t', 1)
        try:
                count = int(count)
        except error:
                continue
        # If this line contains the same word as the line before 
        # increment the running count
        if current == word:
                current_count += count
        # else if we have a word already, print it and its total count, then
        # start a fresh count for the new word in line
        else:
                if current:
                        print current + '\t' + str(current_count)
                current_count = count
                current = word

if current == word:
        print current + '\t' + str(current_count)



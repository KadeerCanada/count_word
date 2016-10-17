#!/usr/bin/python
import sys
in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[2], "w")
from collections import defaultdict
my_count = defaultdict(lambda: 0)

for line in in_file:
    words = line.strip().split(" ")
    for word in words:
        if len(word) > 0:
            my_count[word] +=1
for word, count in sorted(my_count.items()):
    out_file.write("%s\t%r\n" % (word,count))

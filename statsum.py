#!/usr/bin/python3

# this python script will might take over
# right now it just adds statsums

import fileinput

for line in fileinput.input():
	line = line.strip()
	fields = line.split(',')
	statsum = 0
	
	for i in range(0, 5):
		statsum += int(fields.pop())
	print("{},{}".format(line, statsum))


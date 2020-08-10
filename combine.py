#! /usr/local/bin/python3

import sys
import math

def main():
	pairs = {}

	# combine
	for i in range(1, len(sys.argv)):
		f = open(sys.argv[i], 'r')
		lines = f.readlines()

		for line in lines:
			x = float(line.split(' ')[0])
			y = float(line.split(' ')[1])
			
			if str(x) in pairs:
				pairs[str(x)] += float(pairs[str(x)]) + y
			else:
				pairs[str(x)] = y

	# print
	for pair in pairs:
		print(pair, pairs[pair])

main()

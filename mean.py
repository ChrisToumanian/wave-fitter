#! /usr/local/bin/python3

import sys
import math

def main():
	y_vals = []
	
	file1 = open(sys.argv[1], 'r')
	lines = file1.readlines()

	for line in lines:
		y_vals.append(float(line.split(' ')[1]))

	n = len(y_vals)
	mean = float(sum(y_vals) / max(n, 1))

	print(str(mean))

main()

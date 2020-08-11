#! /usr/local/bin/python3

import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
	f = open(sys.argv[1], 'r')
	lines = f.readlines()
	x_array = []
	y_array = []
	image_name = "plot"
	y_label = "y"
	x_label = "x"

	# options
	for i in range(len(sys.argv)):
		if (sys.argv[i] == "-o" or sys.argv[i] == "-out"):
			image_name = str(sys.argv[i + 1])
	for i in range(len(sys.argv)):
		if (sys.argv[i] == "-xlabel"):
			x_label = str(sys.argv[i + 1])
	for i in range(len(sys.argv)):
		if (sys.argv[i] == "-ylabel"):
			y_label = str(sys.argv[i + 1])

	# build arrays
	for line in lines:
		x_array.append(float(line.split(' ')[0]))
		y_array.append(float(line.split(' ')[1]))

	# plot
	plt.ioff()
	fig = plt.figure(figsize=(15, 6))
	plt.title("")
	plt.ylabel(y_label)
	plt.xlabel(x_label)
	plt.grid(True)
	plt.scatter(x_array, y_array, color='b', s=0.1)
	plt.savefig(image_name + '.png')
	plt.close(fig)

main()

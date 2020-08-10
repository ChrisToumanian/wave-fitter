#! /usr/local/bin/python3

import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
	amplitude = 1
	frequency = 1
	vertical_shift = 0
	phase = 0
	range_a = 0
	range_b = 10
	step = 0.01
	x = range_a
	x_array = []
	y_array = []
	image_name = ""

	# input
	for i in range(len(sys.argv)):
		if (sys.argv[i] == "-A" or sys.argv[i] == "-amplitude"):
			amplitude = float(sys.argv[i + 1])
		if (sys.argv[i] == "-f" or sys.argv[i] == "-frequency"):
			frequency = float(sys.argv[i + 1])
		if (sys.argv[i] == "-v" or sys.argv[i] == "-vertical"):
			vertical_shift = float(sys.argv[i + 1])
		if (sys.argv[i] == "-p" or sys.argv[i] == "-phase"):
			phase = float(sys.argv[i + 1])
		if (sys.argv[i] == "-a" or sys.argv[i] == "-rangea"):
			range_a = float(sys.argv[i + 1])
		if (sys.argv[i] == "-b" or sys.argv[i] == "-rangeb"):
			range_b = float(sys.argv[i + 1])
		if (sys.argv[i] == "-i" or sys.argv[i] == "-image"):
			image_name = str(sys.argv[i + 1])
		if (sys.argv[i] == "-h" or sys.argv[i] == "-help" or sys.argv[i] == "help"):
			print("Help:\n-A    amplitude\n-f    frequency\n-v    vertical shift\n-p    phase\n-a    range a\n-b    range b\n-i    image name")
			exit()

	# generate wave
	while x <= range_b:
		# y = A * sin(pi / frequency * x + phase) + vert
		y = float(amplitude * math.sin(math.pi / (frequency / 2) * x + phase * math.pi) + vertical_shift)
		x_array.append(x)
		y_array.append(y)
		print(x, y)
		x += step

	# export plot
	if len(image_name) > 0:
		plt.ioff()
		fig = plt.figure(figsize=(15, 6))
		plt.title("Plot")
		plt.ylabel("amplitude (y)")
		plt.xlabel("time (x)")
		plt.grid(True)
		plt.plot(x_array, y_array)
		plt.savefig(image_name + '.png')
		plt.close(fig)

main()

#! /usr/local/bin/python3

import sys
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy, scipy
from scipy.optimize import curve_fit

def func(x, amplitude, center, width):
	return amplitude * numpy.sin(numpy.pi * (x - center) / width)

def main():
	f = open(sys.argv[1], 'r')
	lines = f.readlines()
	xData = []
	yData = []
	image_name = "plot"

	# options
	for i in range(len(sys.argv)):
		if (sys.argv[i] == "-o" or sys.argv[i] == "-out"):
			image_name = str(sys.argv[i + 1])

	# build arrays
	for line in lines:
		xData.append(float(line.split(' ')[0]))
		yData.append(float(line.split(' ')[1]))

	# estimated from a scatterplot of the data
	initialParameters = numpy.array([-1.0, 180.0, 180.0])
	
	# curve fit the test data
	fittedParameters, pcov = curve_fit(func, xData, yData, initialParameters)

	modelPredictions = func(xData, *fittedParameters) 

	absError = modelPredictions - yData	

	SE = numpy.square(absError) # squared errors
	MSE = numpy.mean(SE) # mean squared errors
	RMSE = numpy.sqrt(MSE) # Root Mean Squared Error, RMSE
	Rsquared = 1.0 - (numpy.var(absError) / numpy.var(yData))

	print('Parameters:', fittedParameters)
	print('RMSE:', RMSE)
	print('R-squared:', Rsquared)

	print()	

	

main()

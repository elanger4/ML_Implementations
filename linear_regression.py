import sys
import numpy as np

"""
    A file to import 2-d data to perform linear regression to predict a specified
    point
"""

if not len(sys.argv) == 3:
    print("ERROR: Incorrect usage\n Usage: ./python linear_regression <datafile> <prediction>")

int_rates = []
price = []

# in_data = 
for line in open(sys.argv[1], 'r'):
	line = line.split('\t')
	int_rates.append(float(line[1]))
	price.append(float(line[2][1:].replace(',','')))

rate_mean = sum(int_rates) / len(int_rates)
price_mean = sum(price) / len(price)

Sxy = 0.0
Sxx = 0.0
for i, j in zip(int_rates, price):
	Sxy += (i - rate_mean) * (j - price_mean)
	Sxx += (i - rate_mean) ** 2

b1 = Sxy / Sxx
b0 = price_mean - (b1 * rate_mean)

y_predict = b0 + b1 * float(sys.argv[2])
print ("Predicted value is: ", y_predict)

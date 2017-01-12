# TODO: import file(s) where stats functions are from

def predict(alpha, beta, x_i):
	return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
	return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
	return sum(error(alpha, beta, x_i, y_i) ** 2
				for x_i, y_i in zip(x,y))

def least_squares_fit(x, y):
	beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
	alpha = mean(y) - beta * mean(x)
	return alpha, beta

def total_sum_of_squares(y):
	return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
	return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
				  total_sum_of_squares(y))

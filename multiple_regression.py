import random
# TODO: some imports I forgot

def predict(x_i, beta):
	return dot(x_i, beta)

def error(x_i, y_i, beat):
	return y_i - predict(x_i, beta)

def squared_error(x_i, y_i, beta):
	return error(x_i, y_i, beta) ** 2

def sqaured_error_gradient(x_i, y_i, beta):
	return [-2 * x_ij * error(x_i, y_i, beta)
			for x_ij in x_i]

def estimate_beta(x, y):
	beta_initial = [random.random() for x_i in x[0]]
	return minimize_stochastic(squared_error,
							   squared_error_gradient, x, y
								beta_initial, 0.001)

def multiple_r_squared(x, y, beta):
	sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2
								for x_i, y_i in zip(x,y))
	return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)

def bootstrap_sample(data):
	return [random.choice(data) for _ in data]

def bootstrap_statistic(data, stats_fn, num_samples):
	return [stats_fn(bootstrap_sample(data))
			for _ in range(num_samples)]

def estimate_sample_beta(sample):
	x_sample, y_sample = zip(*sample)
	return estimate_beta(x_sample, y_sample)

def ridge_penalty(beta, alpha):
	return alpha * dot(beta[1:], beta[1:])

def squared_error_ridge(x_i, y_i, beta, alpha):
	return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)

def ridge_penalty_gradient(beta, alpha):
	return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]

def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
	return vector_add(squared_error_gradient(x_i, y_i, beta),
					  ridge_penalty_gradient(beta, alpha))

def estimate_beta_ridge(x, y, alpha):
	beta_initial = [random.random() for x_i in x[0]]
	return minimize_stochastic(partial(squared_error_ridge, alpha=alpha),
							   partial(squared_error_ridge_gradient,
									   alpha=alpha),
								x, y, beta_initial, 0.001)
				

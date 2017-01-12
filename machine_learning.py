import random

def split_data(data, prob):
	""" split data into fractions [prob, 1 - prob] """
	results = [], []
	for row in data:
		results[0 if random.random() < prob else 1].append(row)
	return results	

def train_test_split(x, y, test_pct):
	data = zip(x,y)
	train, test = split_data(data, 1 - test_pct) 	# Pair corresponding values
	x_train, y_train = zip(*train)					# Split the data set of pairs
	x_test, y_test = zip(*test)						# Magical unzip trick
	return x_train, x_test, y_train, y_test

""" Example Usage:

model = SomeKindOfModel()
x_train, x_test, y_train, y_test = train_test_splt(xs, ys, 0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)
"""

def accuracy(tp, fp, fn, tn):
	correct = tp + tn
	total = tp + fp + fn + tn
	return correct / total

def precision(tp, fp, fn, tn):
	return tp / (tp + fp)

def recall(tp,fp, fn, tn):
	return tp / (tp + fn)

def f1_score(tp, fp, fn, tn):
	p = precision(tp, fp, fn, tn)
	r = recall(tp, fp, fn, tn)


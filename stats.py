import math
from collections import Counter
from linear_algebra import sum_of_squares

def mean(x):
  return sum(x) / len(x)

def median(v):
  """
  Finds the 'middle-most' value
  """
  n = len(v)
  sorted_v = sorted(v)
  midpoint =  n // 2

  if n % 2 == 1:
    return sorted_v[midpoint]
  else:
    lo = midpoint - 1
    hi = midpoint
    return (sorted_v[lo] + sorted_v[hi])

def quantile(x, p):
  """
  Returns the pth-percentile value in x
  """
  p_index = int(p * len(x))
  return sorted(x)[p_index]

a = [1,1,2,2,3,4,4,5,6,8,8,6,5,4,2,2,4,6,5,4,33,5,7,]

def mode(x):
  """
  Return a list, maybe more than one mode
  """
  counts = Counter(x)
  print counts
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.iteritems() if count == max_count]

def data_range(x):
  return max(x) - min(x)

def de_mean(x):
  """
  Translate x by subtrating its mean (result has mean 0)
  """
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]

def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
  return math.sqrt(variance(x))

def interquartile_range(x):
  return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y))

def correlation(x, y):
  stddev_x = standard_deviation(x)
  stddev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x,y) / stdev_x / stdev_y
  else:
    return 0   # if no variation, correlation is zero

def normalize(x):
    x_mean = mean(x)
    x_std = standard_deviation(x)
    return [(i - x_mean) / x_std for i in x]

a = [1,1,2,2,3,4,4,5,6,8,8,6,5,4,2,2,4,6,5,4,33,5,7,]
print 'mode: ', mode(a)



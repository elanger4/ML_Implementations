from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def uniform_pdf(x):
  return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
  """
  Returns the probability that a uniform random variable is <= x
  """
  if x < 0:   return 0  # Uniform random is never < 0
  elif x < 1: return x  # P(X <= 0.4) = 0.4
  else:       return 1  # Uniform random is always <= 1

def normal_pdf(x, mu=0, sigma=1):
  sqrt_two_pi = math.sqrt(2 * math.pi)
  return (math.exp(-(x-mu) ** 2 / 2/ sigma ** 2) / (sqrt_two_pi * sigma))

def normal_cdf(x, mu=0, sigma=1):
  return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
  """
  Find approximate inverse using binary search
  """
  if mu != 0 or sigma != 1:
    return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

  low_z, low_p = -10.0, 0         # normal_cdf(-10) is basically 0
  hi_z,  hi_p  = 10.0, 0          # normal_cdf(10)  is basically 1
  while hi_z - low_z > tolerance:
    mid_z = (low_z + hi_z) / 2    # Consider the midpoint
    mid_p = normal_cdf(mid_z)     # and the cdf's value
    if mid_p < p:
      # Midpoint is low, search above
      low_z, low_p = mid_z, mid_p
    elif mid_p > p:
      # Midpoint is high, search below
      hi_z, hi_p = mid_z, mid_p
    else:
      break
  return mid_z

def bernoulli_trial(p):
  return 1 if random.random() < p else 0

def binomial(n, p):
  return sum(bernoulli_trial(p) for _ in range(n))

def normal_cdf(x, mu=0, sigma=1):
  return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def make_hist(p, n, num_points):
  data = [binomial(n, p) for _ in range(num_points)]

  # Use a bar chart to show the actual binomial samples
  histogram = Counter(data)
  print histogram
  plt.bar([x - 0.4 for x in histogram.keys()],
          [v / num_points for v in histogram.values()],
          0.8,
          color = '0.75')

  mu = p * n
  sigma = math.sqrt(n * p * (1-p))

  # Use a line chart to show the normal approximation
  xs = range(min(data), max(data) + 1)
  ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
                  for i in xs]
  plt.plot(xs,ys)
  plt.title("Binomial Distribution vs. Normal Approximation")
  print 'Showing plt'
  plt.show()

make_hist(0.75, 100, 10000)

from collections import Counter

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

a = [1,1,2,2,3,4,4,5,6,8,8,6,5,4,2,2,4,6,5,4,33,5,7,]
print 'mode: ', mode(a)



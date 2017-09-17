import math

# Vectors ---------------------
def vector_add(v, w):
  """
  Adds corresponding elements
  """
  return [v_i + w_i
         for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
  """
  Subtracts corresponding elements
  """
  return [v_i - w_i
         for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
  """
  Sums all corresponding elements
  """
  return reduce(vector_add, vectors)

def scalar_mulitply(c, v):
  """
  c is a number, v is a vector
  """
  return [c * v_i for v_i in v]

def vector_mean(vectors):
  """
  Compute the vector whose ith element is the mean of the ith elements
  of the input vectors
  """
  n = len(vectors)
  return scalar_mulitply(1/n, vector_sum(vectors))

def dot(v, w):
  """
  v_1 * w_1 + ... + v_n * w_n
  """
  return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
  """
  v_1 * v_1 + ... + v_n * v_n
  """
  return dot(v,v)

def magnitude(v):
  return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
  """"
  (v_1 * v_1) ** 2 + ... + (v_n * v_n) ** 2
  """
  return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
  return math.sqrt(square_distance(v,w))

# Matrices -------------------------------------------------

def shape(A):
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0
  return num_rows, num_cols

def get_row(A, i):
  return A[i]

def get_column(A, i):
  return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
  """
  Returns a num_rows x num_cols matrix whose 
  (i,j)th entry us entry_fn(i,j)
  """
  return [[ entry_fn(i, j)
          for j in range(num_cols)]
          for i in range(num_rows)]

def is_diagonal(i, j):
  """
  1s on the diagonal, 0s elsewhere
  """
  return 1 if i == j else 0

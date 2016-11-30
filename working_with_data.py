
def de_mean_matrix(A):
  nr, nc = shape(A)
  column_means, _ = scale(A)
  return make_matrix(nr, nc, lambda i, j: A[i][j] - columns_means[j])

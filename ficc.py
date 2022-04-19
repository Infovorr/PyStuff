def ficc(n):
  if n < 3:
    return 1
  return ficc(n - 1) + ficc(n - 2)

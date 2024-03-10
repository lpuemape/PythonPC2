def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(51):
  numero_fibonacci = fibonacci(i)
  print(numero_fibonacci)

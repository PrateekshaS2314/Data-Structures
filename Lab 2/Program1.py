def fibo(n):
  if n == 0:
    return 0
  elif n == 10:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)
n=6
result = fibo(n)
print(result)

#Recursion

#Factorial


def factorial(n):
  if (n == 0):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(0))
print(factorial(3))
print(factorial(5))
print(factorial(1))

# Fibonacci sequence   (some doubt #tutorial 30) not completed
# Fibonacci sequence means
#ex - f(2) = f(1)+f(0)
#     f(4) = f(3)+f(2)+f(1)+f(0)


def fibonaccisequence(m):
  if (m == 0):
    return 0
  else:
    return m - 1


print(fibonaccisequence(0))
print(fibonaccisequence(2))
print(fibonaccisequence(3))
print(fibonaccisequence(1))
print(fibonaccisequence(4))
print(fibonaccisequence(19))
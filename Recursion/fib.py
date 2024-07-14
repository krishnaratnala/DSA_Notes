'''
print fibonacci series
'''
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Print the Fibonacci series for n = 5
n = 5
fibonacci_series = [fib(i) for i in range(n)]
print(fibonacci_series)


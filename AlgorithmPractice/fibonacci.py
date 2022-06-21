memo = {}
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        try:
            return memo[n]
        except:
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
print(fib(10))
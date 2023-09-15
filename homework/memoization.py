
def memoize(f):
    memoize_cache = {}
    def inner(n):
        if n not in memoize_cache:
            memoize_cache[n] = f(n)
        return memoize_cache[n]
    return inner

@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n -1) + fib(n - 2)

# without decorator
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n -1) + fib2(n - 2)


if __name__ == '__main__': 
    print(fib(5))
    print(fib(30))
    print(fib(50))
    print(fib(80))
    print(fib(500))
    print(fib(800))

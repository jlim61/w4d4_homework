from memoization import memoize

def count_calls(f):
    inner_counter = [0]
    def inner(n):
        inner_counter[0] += 1
        print(inner_counter[0])
        return f(n)
    return inner

@count_calls
@memoize
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n -1) + fib(n - 2)

@count_calls
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n -1) + fib2(n - 2)

# with memoize, it should be lower than without memoize (counter)
fib(5)

print('break')
# should return 15 with fib + count_calls for fib2(5)
fib2(5)

# Function to test my count is accurate. This function will call itself the number of times equal to number I enter as argument
# count calls counts the initial call as well so it should count 11 total calls.
# @count_calls
# def counter_func_test(n):
#     if n <= 0:
#         print("Done")
#         return
#     print(f"Calling counter_func_test({n - 1})")
#     counter_func_test(n - 1)

# if __name__ == '__main__': 
# Call counter_func_test with n = 10, count calls should always give n+1 (11 if n=10)
    # counter_func_test(20)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

is_even = lambda x: x%2==0
print(is_even(4))
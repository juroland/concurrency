''' computation functions to test cpu bound programs'''


def fib(n):
    ''' A slow implementation of Fibonnaci '''
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

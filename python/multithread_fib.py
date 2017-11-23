'''Compute fibonacci numbers with multiple threads to show the GIL'''

import random
import threading
import compute
import syscall

def thread_func_monitor(func):
    def wrapper(*args, **kargs):
        print(f'Function {func.__name__} executed by thread {syscall.gettid()}')
        return func(*args, **kargs)
    return wrapper


@thread_func_monitor
def apply(data, func, start, stop, results):
    '''Apply function func on each element of data in the range [start, stop['''
    results.extend([func(x) for x in data[start:stop]])


def main(nthreads=4):
    numbers = random.choices(population=range(23, 26), k=300)

    chunk = len(numbers) // nthreads
    starts = range(0, nthreads * chunk, chunk)
    stops = list(range(chunk, nthreads * chunk + 1, chunk))
    stops[-1] = len(numbers)

    threads = []
    threads_results = []
    for start, stop in zip(starts, stops):
        threads_results.append([])
        results = threads_results[-1]
        t = threading.Thread(target=apply, args=(numbers, compute.fib, start, stop, results))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    for results in threads_results:
        print(' -> ', results)


if __name__ == '__main__':
    main()
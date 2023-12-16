from time import time


# create a decorator to measure the time of a function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        output = func(*args, **kwargs)
        end_in_str = str(time() - start)
        print(f'Time elapsed: {end_in_str} seconds')
        return output
    return wrapper

@measure_time
def find_primes_until(n: int) -> list[int]:
    """Returns all the prime numbers until n"""
    primes = [2, 3]
    for i in range(3, n, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


@measure_time
def optimised_prime_counter(n: int) -> list[int]:
    """Returns all the prime numbers until n"""
    primes = [2, 3]
    cache = []
    current = 3
    while current < n - 1:
        next = min(primes[-1] ** 2, n)
        for i in range(current, next, 2):
            for j in primes:
                if i % j == 0:
                    break
            else:
                cache.append(i)
        primes.extend(cache)
        current = next
        cache = []
    return primes
    

def main():
    """
    n = 100_000 -> 1.4387047290802002 seconds
    n = 1_000_000 -> 101.03466010093689 seconds
    """
    n = 1000000
    #primes = find_primes_until(n)
    o_primes = optimised_prime_counter(n)
    #print(primes)

if __name__ == '__main__':
    main()
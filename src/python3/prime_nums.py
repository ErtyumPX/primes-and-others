from defaults import measure_time, timer


@measure_time
def prime_finder(n: int) -> list[int]:
    """Returns all the prime numbers until n"""
    primes: list = [2, 3]
    for i in range(3, n, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


@measure_time
def optimised_prime_finder(n: int) -> list[int]:
    """Returns all the prime numbers until n"""
    primes: list = [2, 3]
    cache: list = []
    current: int = 3
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
    find_primes_until:
    n = 100_000 -> 1.4387047290802002 seconds
    n = 1_000_000 -> 101.03466010093689 seconds

    optimised_prime_counter:
    n = 100_000 -> 0.10260200500488281 seconds
    n = 1_000_000 -> 0.9501941204071045 seconds
    """
    n = 100_000
    prime_finder(n)
    optimised_prime_finder(n)


if __name__ == '__main__':
    main()
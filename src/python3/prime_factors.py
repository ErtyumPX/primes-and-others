from math import floor, sqrt
from defaults import measure_time
from prime_nums import optimised_prime_finder


@measure_time
def list_of_prime_factors(n: int) -> list[int]:
    """Returns all the prime factors of n"""
    factors: list = []
    primes: list = optimised_prime_finder(floor(sqrt(n)))
    i = 0
    while i < len(primes): 
        if n % primes[i] == 0:
            n //= primes[i]
            factors.append(primes[i])
            i -= 1
        i += 1
    if n != 1:
        factors.append(n)
    return factors


@measure_time
def set_of_prime_factors(n: int) -> set[int]:
    """Returns a set of all the prime factors of n"""
    factors: set = set()
    primes: list = optimised_prime_finder(floor(sqrt(n)))
    i = 0
    while i < len(primes): 
        if n % primes[i] == 0:
            n //= primes[i]
            factors.add(primes[i])
        i += 1
    if n != 1:
        factors.add(n)
    return factors


def main():
    factors_list = list_of_prime_factors(15281913531865)
    print(factors_list)
    factors_set = set_of_prime_factors(15281913531865)
    print(factors_set)

if __name__ == '__main__':
    main()
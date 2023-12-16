from defaults import measure_time, timer


@measure_time
def factorial(n: int) -> int:
    """
    Returns the factorial of n.
    """
    assert n >= 0, "n must be a positive integer"
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


@measure_time
def combination_count(n: int, k: int) -> int:
    """
    Returns the number of combinations of n elements taken k at a time.
    """
    assert n >= 0, "n must be a positive integer"
    assert k >= 0, "k must be a positive integer"
    assert n >= k, "n must be greater than or equal to k"
    return factorial(n) // (factorial(k) * factorial(n - k))


@measure_time
def combinations(n: int, k: int) -> list[list[int]]:
    """
    Returns a list of all the combinations of n elements taken k at a time.
    """
    output: list[list[int]] = []
    
    return output


def main():
    n = 10
    k = 4
    #fact = factorial(n)
    #print(fact)

    #comb_count = combination_count(n, k)
    #print(comb_count)

    comb = combinations(n, k)
    print(comb)
    print(len(comb))


if __name__ == '__main__':
    main()
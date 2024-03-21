import timeit

"""
Implement 3 different algorithms for computing the greatest common divisor of 2 natural numbers.
One of the algorithms should work for numbers of arbitrary size!
Perform a comparative running-time analysis of these algorithms for a set of at least 10 inputs (use
appropriate time units in order to differentiate the algorithms).
"""


def euclidean(a, b):
    while b:
        a, b = b, a % b
    return a


def recursive_euclidean(a, b):
    if b == 0:
        return a
    else:
        return recursive_euclidean(b, a % b)


def steins(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    # Initialize common factors of 2
    common_factors_of_2 = 0

    while a % 2 == 0 and b % 2 == 0:
        a //= 2
        b //= 2
        common_factors_of_2 += 1

    while a != b:
        if a % 2 == 0:
            a //= 2
        elif b % 2 == 0:
            b //= 2
        elif a > b:
            a = (a - b) // 2
        else:
            b = (b - a) // 2

    return a * (2 ** common_factors_of_2)

# List of input pairs
pairs = [(120, 72), (48, 18), (1071, 462), (0, 48), (12345, 67890), (123456, 98765), (1234567, 9876543),
         (12345678, 98765432), (123456789, 987654321), (9876543210, 1234567890)]

# Compare the running times of the three GCD algorithms for each pair
for a, b in pairs:
    print(f"Input: ({a}, {b})")

    # Using the Euclidean algorithm
    euclidean_time = timeit.timeit(lambda: euclidean(a, b), number=1000)
    print(f"Euclidean GCD: {euclidean(a, b)}, Time: {euclidean_time:.6f} seconds")

    # Using the recursive Euclidean algorithm
    recursive_euclidean_time = timeit.timeit(lambda: recursive_euclidean(a, b), number=1000)
    print(f"Recursive Euclidean GCD: {recursive_euclidean(a, b)}, Time: {recursive_euclidean_time:.6f} seconds")

    # Using the math.gcd function
    gcd_math_time = timeit.timeit(lambda: steins(a, b), number=1000)
    print(f"math.gcd GCD: {steins(a, b)}, Time: {gcd_math_time:.6f} seconds")
    print()

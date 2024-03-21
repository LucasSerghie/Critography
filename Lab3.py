"""This is an implementation of the Miller-Rabin algorithm."""


def miller_rabin_test(_number):
    s = 0
    t = _number - 1
    while not t & 1:
        s += 1
        t //= 2

    for a in [2, 3, 5, 7, 11, 13]:
        while t < _number - 1:
            if pow(a, t, _number) == 1:
                return True
            t *= 2

    return False


number = int(input("Enter a number: "))
print(miller_rabin_test(number))

import math
from datetime import datetime

MAX_NUMBER = 10
PRIME_CONSTANT_A = 11
PRIME_CONSTANT_C = 3


def checkModulus(max_num):
    return max_num > 0


def checkCoprimes(m, c):
    return math.gcd(m, c) == 1


def primeFactorsCheck(max_num, const_a):
    prime_factors = set()
    while max_num % 2 == 0:
        prime_factors.add(2)
        max_num //= 2

    for i in range(3, int(math.sqrt(max_num)) + 1, 2):
        while max_num % i == 0:
            prime_factors.add(i)
            max_num //= i

    if max_num > 2:
        prime_factors.add(max_num)

    for i in prime_factors:
        if (const_a - 1) % i != 0:
            return False

    return True


def divisibleByFour(max_num, a_num):
    if max_num % 4 != 0:
        return True

    if (a_num - 1) % 4 == 0:
        return True
    else:
        return False


if not checkModulus(MAX_NUMBER):
    raise ValueError("Modulus must be positive")

if not checkCoprimes(MAX_NUMBER, PRIME_CONSTANT_C):
    raise ValueError("Coprime condition invalid")

if not primeFactorsCheck(MAX_NUMBER, PRIME_CONSTANT_A):
    raise ValueError("Prime factor condition invalid")

if not divisibleByFour(MAX_NUMBER, PRIME_CONSTANT_A):
    raise ValueError("Divisible by four condition invalid")

seed = int(datetime.now().timestamp())

ran_num = seed % MAX_NUMBER

ran_num = (PRIME_CONSTANT_A * ran_num + PRIME_CONSTANT_C) % MAX_NUMBER

print(ran_num)

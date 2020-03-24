import math


def countPrimes(n):
    if n < 2:
        return 0
    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0
    for i in range(2, int(math.sqrt(n))):
        if isPrime[i] != 0:
            for j in range(i * i, n, i):
                isPrime[j] = 0

    return [c for c, v in enumerate(isPrime) if v != 0]


print(countPrimes(10))

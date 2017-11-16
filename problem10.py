import time
import math


def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    span = int(math.sqrt(n)) + 1
    while(i < span):
        if n % i == 0:
            return False
        i += 1
    return True


def sum_of_primes(n):
    total = 0
    i = 2
    while i < n:
        if is_prime(i):
            total += i
        i += 1
    return total


def main():
    s = time.time()
    result = sum_of_primes(2000000)
    print('sum of first 2 million primes is: ', result)
    print('total time taken: ', time.time() - s)


if __name__ == '__main__':
    main()

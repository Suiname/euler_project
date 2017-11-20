import time
import math


def nth_tri_num(n):
    return sum(range(n+1))


def factorization(n):
    if n == 1:
        return [n]
    factors = [1, n]
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            if n != i:
                factors.append(i)
                factors.append(int(n/i))
            else:
                factors.append(i)
        i += 1
    return factors


def tri_factors_over(n):
    i = 1
    tri_num = nth_tri_num(i)
    while len(factorization(tri_num)) < n:
        i += 1
        tri_num = nth_tri_num(i)
    return tri_num


def main():
    s = time.time()
    print('triangle number with over 500 factors: ', tri_factors_over(500))
    print('total time taken: ', time.time() - s)


if __name__ == '__main__':
    main()

import math


def pyt_triplet(a, b):
    c = math.sqrt(a*a + b*b)
    return c


def sum_triplets(a, b):
    c = pyt_triplet(a, b)
    return a + b + c


def find_triplet(total):
    a = 1
    b = 1
    while sum_triplets(a, b) != total:
        if sum_triplets(a, b) >= total:
            a = 1
            b += 1
        else:
            a += 1
    return a, b, pyt_triplet(a, b)


def main():
    triplet = find_triplet(1000)
    print(triplet[0] * triplet[1] * triplet[2])


if __name__ == '__main__':
    main()
